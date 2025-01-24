import copy
import numpy as np
import pandas as pd

from padtest.geometry.plate import SymmetricPlateGeometry as SG
from padtest.geometry.plate import NonSymmetricPlateGeometry as NSG
from padtest.model.model import Model

class PlateModel():
    """Based class with shared methods of shallow foundaiton Plaxis
    models with plate elements for the structure."""

    def __init__(self):
        """Initialize a new instance of `PlateModel`.
        """

    #===================================================================
    # PRIVATE METHODS
    #===================================================================
    def _init_foundation_material(self, footing, column):
        """Initializes plate materials.

        Parameters
        ----------
        footing : dict
            Dictionary with the properties of the material used in 
            the footing.
        column : dict, None
            Dictionary with the properties of the material used in 
            the footing. For surface foundaitons None.
        """
        footing['Identification'] = 'footing'
        self._plate_material['footing'] = copy.deepcopy(footing)
        if column is not None:
            column['Identification'] = 'column'
            self._plate_material['column'] = copy.deepcopy(column)

    def _build_load(self):
        """Adds the foundation load to the model.
        """
        self._load = self._g_i.pointload([0, 0])
    
    def _build_surface_load(self):
        """Adds surface load to the model.
        """
        self._surface_load = []
        load =  self._g_i.lineload([self._xlim[0], 0], [self._xlim[1], 0])
        self._surface_load.append(load)

    def _set_load(self, load):
        """Sets load value in the current phase.

        Parameters
        ----------
        load : np.ndarray
            (3,) with (Fy, Fx, M) applied to the foundaiton.
        
        Raises
        ------
        RuntimeError
            Non vertical load in symmetric model.
        """

        self._g_i.activate(self._g_i.PointLoad_1_1, self._g_i.Model.CurrentPhase)
        self._g_i.set(self._g_i.PointLoad_1_1.Fy, self._g_i.Model.CurrentPhase, load[0])
        self._g_i.set(self._g_i.PointLoad_1_1.Fx, self._g_i.Model.CurrentPhase, load[1])
        self._g_i.set(self._g_i.PointLoad_1_1.M, self._g_i.Model.CurrentPhase, load[2])
        # self._g_i.activate(self['load'][0], self._g_i.Model.CurrentPhase)
        # self._g_i.set(self['load'][1].Fy, self._g_i.Model.CurrentPhase, load)

    def _set_surface_load(self, qsurf):
        """Activates and sets a value to the surface load in the
        curernt phase. 

        Parameters
        ----------
        qsurf : numeric
            Surface load.
        """

        self._g_i.activate(self._g_i.LineLoad_1_1, self._g_i.Model.CurrentPhase)
        self._g_i.set(self._g_i.LineLoad_1_1.qy_start, self._g_i.Model.CurrentPhase, qsurf)

    def _activate_foundation(self, phaseidx):
        """Activates the foundation.

        Parameters
        ----------
        phaseidx : int
            Intex of the phase object in which the foundation is
            activated.
        """
        self._g_i.gotostructures()
        self._footing_plx[-1].setmaterial(self._plate_material_plx['footing'])
        if self._column is not None:
            self._column_plx[-1].setmaterial(self._plate_material_plx['column'])
        self._g_i.gotostages()
        self._g_i.activate(self._footing_plx[2], self._g_i.phases[phaseidx])
        if self._column is not None:
            self._g_i.activate(self._column_plx[2], self._g_i.phases[phaseidx])
    
    def _set_output_precalc(self):
        """Select output points before calcualtion. Used for points in
        the soil."""
        pass
    
    def _set_output_postcalc(self):
        """Select output points before calcualtion. Used for points in
        structural elements."""        
        plate_column = self._g_o.get_equivalent(self._g_i.Plate_1_1)        
        self._output_point['top'] = self._g_o.addcurvepoint("node", plate_column, (0, 0))
        
        for loc, xcoord in zip(self._output_location, self._output_location_xcoord):
            if self._d == 0:
                plate_footing = self._g_o.get_equivalent(self._g_i.Plate_1_1)
            elif self._symmetric or (not self._symmetric and loc<=0):
                plate_footing = self._g_o.get_equivalent(self._g_i.Plate_2_1)
            else:
                plate_footing = self._g_o.get_equivalent(self._g_i.Plate_2_2)
            self._output_point[loc] = self._g_o.addcurvepoint("node", plate_footing, (xcoord,  -self._d))
        
    def _extract_initial_phase_results(self, phaseid, nstep):
        """Extracts results form the output of the initial phases calculation.

        Parameters
        ----------
        phaseid : str
            Phase id.
        nstep : int
            Number of steps in the phase.

        Returns
        -------
        np.ndarray
            (nstep, 1) sumMstage of the phase.
        np.ndarray
            (nstep, nloc) uy displacement at the output locations.
        np.ndarray
            (nstep, nloc) ux displacement at the output locations.
        """

        Uy = np.zeros((len(self._output_location) + 1, nstep))
        Ux = np.zeros((len(self._output_location) + 1, nstep))
        sumMstage = np.zeros(nstep)

        for sidx, step in enumerate(self._ophases[phaseid].Steps.value):
            sumMstage[sidx] = step.Reached.SumMstage.value
            for locidx, node in enumerate(self._output_point.keys()):
                Uy[locidx, sidx] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Soil.Uy)
                Ux[locidx, sidx] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Soil.Ux)
        return sumMstage, Uy, Ux
    
    def _set_phase_results(self, testid, phaseid, prevphaseid, load):
        """Adds phase results to the results dataframe.

        Parameters
        ----------
        testid : str
            Test id.
        phaseid : str
            Phase id
        prevphaseid : str
            Id of the previous phase.
        load : np.ndarray
            (3,) load applied at the end of the phase (Fy, Fx, M).
        """

        iphase = self._iphases[phaseid]
        previphase = self._iphases[prevphaseid]
        ophase = self._ophases[phaseid]
        prevophase = self._ophases[prevphaseid]

        nstep = len(list(ophase.Steps.value))
        steps = np.linspace(0, nstep, nstep + 1)
        time = np.zeros(nstep + 1)
        sumMstage = np.zeros(nstep + 1)
        SumMsf = np.zeros(nstep + 1)
        qy0 = np.zeros(nstep + 1)
        qy1 = np.zeros(nstep + 1)
        qx = np.zeros(nstep + 1)
        Fy = np.zeros(nstep + 1)
        Fx = np.zeros(nstep + 1)
        M = np.zeros(nstep + 1)
        base_accel_x = np.zeros(nstep + 1)
        base_accel_y = np.zeros(nstep + 1)
        Fy_target = np.zeros(nstep + 1)
        Fx_target = np.zeros(nstep + 1)
        M_target= np.zeros(nstep + 1)
        Uy = np.zeros((len(self._output_location) + 1, nstep + 1))
        Ux = np.zeros((len(self._output_location) + 1, nstep + 1))

        self._g_i.view(iphase)
        self._set_output_postcalc()

        # start with last step from previous phase
        step = prevophase.Steps.value[-1]
        for locidx, node in enumerate(self._output_point.keys()):
            Uy[locidx, 0] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Plate.Uy)
            Ux[locidx, 0] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Plate.Ux)
        
        for sidx, step in enumerate(ophase.Steps.value):
            sumMstage[sidx + 1] = step.Reached.SumMstage.value
            SumMsf[sidx + 1] = step.Reached.SumMsf.value
            time[sidx + 1]  = step.Reached.DynamicTime.value
            for locidx, node in enumerate(self._output_point.keys()):
                Uy[locidx, sidx + 1] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Plate.Uy)
                Ux[locidx, sidx + 1] = self._g_o.getcurveresults(self._output_point[node], step, self._g_o.ResultTypes.Plate.Ux)
        
        target_load_start = self._get_phase_load(prevphaseid, 'end')
        # Target loads
        Fy_target = target_load_start[0] + (load[0] - target_load_start[0]) * sumMstage
        Fx_target = target_load_start[1] + (load[1] - target_load_start[1]) * sumMstage
        M_target = target_load_start[2] + (load[2] - target_load_start[2]) * sumMstage

        Fy_start = 0
        Fx_start = 0
        M_start = 0
        Fy_end = 0
        Fx_end = 0
        M_end = 0
        if self._g_i.PointLoad_1_1.Active[previphase] is not None:
            if self._g_i.PointLoad_1_1.Active[previphase].value:
                Fy_start = self._g_i.PointLoad_1_1.Fy[previphase].value
                Fx_start = self._g_i.PointLoad_1_1.Fx[previphase].value
                M_start = self._g_i.PointLoad_1_1.M[previphase].value
        
        if self._g_i.PointLoad_1_1.Active[iphase] is not None:
            if self._g_i.PointLoad_1_1.Active[iphase].value:
                Fy_end = self._g_i.PointLoad_1_1.Fy[iphase].value
                Fx_end = self._g_i.PointLoad_1_1.Fx[iphase].value
                M_end = self._g_i.PointLoad_1_1.M[iphase].value
                
                Fy = Fy_start + (Fy_end - Fy_start) * sumMstage
                Fx = Fx_start + (Fx_end - Fx_start) * sumMstage
                M = M_start + (M_end - M_start) * sumMstage
        
        # ad results to dataframe
        for locidx, loc in enumerate(self._output_point):
            df = pd.DataFrame({'test':[testid] * (nstep + 1),
                               'phase':[iphase.Identification.value] * (nstep + 1),
                               'previous':[previphase.Identification.value] * (nstep + 1),
                               'plx id':[iphase.Name.value] * (nstep + 1),
                               'previous plx id':[previphase.Name.value] * (nstep + 1),
                               'location': [loc] * (nstep + 1),
                               'step': steps,
                               'time': time,
                               'sumMstage':sumMstage, 
                               'SumMsf':SumMsf,
                               'uy': Uy[locidx, :],
                               'ux': Ux[locidx, :],
                               'Fy': Fy,
                               'Fx': Fx,
                               'M':M,
                               'qy0':qy0,
                               'qy1':qy1,
                               'qx':qx,
                               'agx':base_accel_x,
                               'agy':base_accel_y,
                               'Fy target':Fy_target,
                               'Fx target':Fx_target,
                               'M target':M_target,                               
                               'ratchetting': [False] * (nstep + 1)})
            if len(self._results) == 0:
                self._results = df
            else:
                self._results = pd.concat([self._results, df])
            self._results.reset_index(inplace=True, drop=True)

    def _set_dynamic_load(self, time, load):
        """Sets dynamic load.

        Parameters
        ----------
        time : array-like
            (nt,) time array.
        load : array-like
            (ncomp, nt) force array (Fy, Fx). If only Fy is provided, Fx
            is assumed as 0.

        Returns
        -------
        np.ndarray
            (nt,) time.
        array-like
            Original load input.
        np.ndarray
            (3, nt) Load array (Fy, Fx, M).
    
        Raises
        ------
        RuntimeError
            Time is not 1-dimensional.
        RuntimeError
            More than 10,000 time steps.
        RuntimeError
            Load has horizontal component in symmetric model.
        RuntimeError
            Length of load array does not match the time array.
        """
        if time.ndim != 1:
            raise RuntimeError('Time must be defined by a 1-dimensional array.')
        if len(time) > 10000:
            raise RuntimeError('Number of time steps must be <=10,000.')
    
        nt = time.size
        input_load = copy.deepcopy(load)
        if self._symmetric and load.ndim != 1:
            raise RuntimeError('Symmetric foundations only allow for vertical loading. A 1-dimensional array is required.')
        elif self._symmetric or load.ndim == 1:
            load = np.vstack([load, np.zeros_like(load), np.zeros_like(load)])

        if load.shape[1] != nt:
            msg = 'Load and time arrays must have the same length.'
            raise RuntimeError(msg)
        return time, input_load, load

    def _calculate_dynamic_load_phase(self, time, load):
        """Calcualtes a dynamic load phase.

        Parameters
        ----------
        time : np.ndarray
            (nt,) time array.
        load : np.ndaarray
            (ncom, nt) Applied forces (Fy, Fx, M).

        Returns
        -------
        str
            Calculation status.
        """

        lmFy = self._g_i.loadmultiplier()
        self._g_i.set(lmFy.Signal, "Table")
        for idx, (t, Fy) in enumerate(zip(time, load[0])):
            lmFy.Table.add()
            self._g_i.set(lmFy.Table[idx].Time, t)
            self._g_i.set(lmFy.Table[idx].Multiplier, Fy)
        
        lmFx = self._g_i.loadmultiplier()
        self._g_i.set(lmFx.Signal, "Table")
        for idx, (t, Fx) in enumerate(zip(time, load[1])):
            lmFx.Table.add()
            self._g_i.set(lmFx.Table[idx].Time, t)
            self._g_i.set(lmFx.Table[idx].Multiplier, Fx)

        lmM = self._g_i.loadmultiplier()
        self._g_i.set(lmM.Signal, "Table")
        for idx, (t, M) in enumerate(zip(time, load[2])):
            lmM.Table.add()
            self._g_i.set(lmM.Table[idx].Time, t)
            self._g_i.set(lmM.Table[idx].Multiplier, M)

        self._g_i.activate(self._g_i.DynPointLoad_1_1, self._g_i.Model.CurrentPhase)
        self._g_i.set(self._g_i.DynPointLoad_1_1.Distribution ,self._g_i.Model.CurrentPhase, "Uniform")
        self._g_i.set(self._g_i.DynPointLoad_1_1.Fy, self._g_i.Model.CurrentPhase, 1)
        self._g_i.set(self._g_i.DynPointLoad_1_1.Fx, self._g_i.Model.CurrentPhase, 1)
        self._g_i.set(self._g_i.DynPointLoad_1_1.M, self._g_i.Model.CurrentPhase, 1)
        self._g_i.set(self._g_i.DynPointLoad_1_1.MultiplierFy, self._g_i.Model.CurrentPhase, lmFy)
        self._g_i.set(self._g_i.DynPointLoad_1_1.MultiplierFx, self._g_i.Model.CurrentPhase, lmFx)
        self._g_i.set(self._g_i.DynPointLoad_1_1.MultiplierM, self._g_i.Model.CurrentPhase, lmM)
        
        status = self._g_i.calculate(self._g_i.Model.CurrentPhase)
        return status

    def _set_dynamic_load_result(self, testid, time, load):
        """Adds dynamic load values to results dataframe.

        Parameters
        ----------
        testid : str
            Test id.
        time : np.ndarray
            (nt,) time array.
        load : np.ndarray
            (3, nt) Load array (Fy, Fx, M).
        """
        idx = (self._results['test'] == testid)
        for loc in self._output_point.keys():
            idx2 = idx & (self._results['location']==loc)
            result_time = self._results.loc[idx2, 'time'].to_numpy(dtype='float64')
            self._results.loc[idx2, 'Fy'] = np.interp(result_time, time, load[0])
            self._results.loc[idx2, 'Fx'] = np.interp(result_time, time, load[1])
            self._results.loc[idx2, 'Fx'] = np.interp(result_time, time, load[2])


class SymmetricPlateModel(SG, PlateModel, Model):
    """Shallow symmetric foundaiton Plaxis model with plate elements for
    the structure.

    Parameters
    ----------
    s_i : Server
        Plaxis Input Application remote sripting server.
    g_i : PlxProxyGlobalObject
        Global object of the current open Plaxis model in Input.
    g_o : PlxProxyGlobalObject
        Global object of the current open Plaxis model in Output.
    b : float
        Foundation width [m].
    d : float
        Foundation depth [m].
    soil : soil : dict, list
        Dictionary with the material properties or list of
        dictionaries.
    footing : dict
        Dictionary with the properties of the material used in 
        the footing.
    column : dict, None
        Dictionary with the properties of the material used in 
        the footing. For surface foundaitons None.
    model_type : str, optional
        Model type: 'axisymmetry' or 'planestrain'. By default
        'axisymetry'. By dafault 'axisymmetry'.
    element_type : str, optional
        Element type: '6-Noded' or '15-Noded'. By default
        '15-Noded'.
    title : str, optional
        Model title in Plaxis. By default ''.
    comments : str, optional
        Model comments in Plaxis. By defautl ''.
    dstrata : list, None, optional
        Width of soil layers [m]. By defautl None.
    wt : float, None, optional
        Water tabe depth [m]. By default None.
    fill_angle : float, None, optional
        Fill angle [deg]. By default None.
    bfill : float, optional.
        Distance between foundation edge and the start of the fill
        slope [m]. By default 0.5.
    nfill : int, None, optional
        Number of fill layers. By default None.
    dfill : list, None, optional
        (nfill,) width of fill layers [m]. By default None.
    interface : bool, dict, optional
        Bool activates/deactivates all the interfaces. Otherwise a 
        dictionary with the 'top', 'bottom', 'column' and 'lateral'
        keys can be provided. For each key either a bool is provided
        indicating whether that interface will be considered in the
        model. Also a dict can be provided for each key with the
        soil material to be assigned to it. By default False.
    model_widht : float, None, optional
        User specified model width [m]. By default None.
    model_depth : float, None, optional
        User specified model depth [m]. By default None.
    fill : dict, list, None, optional
        Dictionary with the fill properties or list of dictionaries.
        By default None.
    mesh_density : float, optional
        Mesh density. By default 0.06.
    dratchetting : float, optional
        Widht of soil under the foundation that is replaced when
        ratchetting occurs [m]. By default 0.
    ratchetting_material  : dict, None, optional
        Dictionary with the material properties after ratchetting.
    ratchetting_threshold : float, optional
        Upwards displacement threshold that when surpassed by any
        output location under the foundation the material under
        it is replaced by the ratchetting material. By default
        np.inf.
    locations : array-like, optional
        (nloc, 1) location of output points in the foundation
        bottom, measured as [0, 1] where 0 is the center of the
        foundation and 1 the edge. By default
        [0, 0.25, 0.5, 0.75, 1].
    build : bool, optional
        Builds Plaxis model automatically. By default True.
    excavation : bool, optional
        If True in models with fill, the excavation and fill
        processes are included in the initial phases. By default
        True.
    deformation_boundary_condition : dict, None, optional
        Deformation boundary conditions of the model. If None the
        default setting is adopted. Dictionary with keys `XMin`,
        `XMax`, `YMin` and `YMax`, with supported values
        'Free',  'Normally fixed',  'Horizontally fixed',
        'Vertically fixed' and 'Fully fixed'. By default None.
    dynamic_boundary_condtions : dict, None, optional
        Dynamic boundary conditions of the model used in dynamic load
        tests. If None the default setting is adopted. Dictionary
        with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
        values 'None' and 'Viscous'. By default None.
    shake_boundary_condtions : dict, None, optional
        Dynamic boundary conditions of the model used in base shake
        tests. If None the default setting is adopted. Dictionary
        with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
        values 'None', 'Viscous', 'Free-field' and 'Compliant base'.
        By default None.
    boundary_interface : bool, optional
        Include boundary interfaces needed for a base shake test.
        This requires a much denser mesh and more computationally
        demanding models. By default False.
    
    Methods
    -------
    build()
        Builds the model in Plaxis.
    regen(s_i, g_i, g_o, test=False) : 
        Regenerates the model in Plaxis. Optinoally it recalculates
        previous load tests.
    save(filename)
        Saves model to file. Plaxis objects cannot be stored, only
        input properties and results. When loaded, the model can
        be regenerated with <regen> method.
    load(filename)
        Loads saved test.
    failure_test(testid, load, max_load=[np.inf, np.inf, np.inf], load_factor=2, load_increment=[0, 0, 0], qsurf=None, start_from='construction', delete_fail=True)
        Test the foundation until the model does not converge.
    load_test(testid, load, start_from='construction', qsurf=None, delete_fail=True)
        Conducts a load test in the model.
    safety_test(testid, start_from, test='incremental', SumMsf=None, Msf=0.1, qsurf=None, delete_fail=True)
        Conducts a safety test on the model.
    dynamic_test(testid, time, load, start_from='construction', nsubstep=10, qsurf=None, delete_fail=True)
        Apply a dynamic load to the foundation.
    shake_test(testid, time, acceleration, start_from='construction', qsurf=None, nsubstep=10, delete_fail=True)
        Apply a displacement time history at the model base.
    delete_test( testid, delete_phases=True) 
        Deletes a test from the model.
    plot(figsize=2.5, foundation=True, fill=True, soil=True, excavation=False, ratchetting=True, wt=True, interface=False, output_location=False)
        Foundation plot.
    plot_test(testid, force=None, displacement=None, phase=None, location=None, compression_positive=True, pullout_positive=False, reset_start=False, legend=False, xlim=None, ylim=None, figsize=(4, 3)) 
        Plots test results.
    plot_safety_test(testid, location=None, pullout_positive=False, reset_start=False, legend=False, figsize=(6, 4))
        Plots safety test.
    plot_dynamic_test(testid, displacement=None, force=None, location=None, compression_positive=True, pullout_positive=False, xlim=None, ylim=None, legend=False, figsize=(8, 2))
        Plot dynamic test resutls versus time.
    plot_shake_test(self, testid, displacement=None, acceleration=None, location=None, pullout_positive=False, xlim=None, ylim=None, legend=False, figsize=(8, 2))
        Plot shake test results versus time.
    """

    _DEFAULT_DEFORMATION_BC = {'XMin':'Horizontally fixed',
                               'XMax':'Horizontally fixed',
                               'YMin':'Fully fixed',
                               'YMax':'Free'}
    _DEFAULT_DYNAMIC_BC = {'XMin':'None',
                           'XMax':'Viscous',
                           'YMin':'Viscous',
                           'YMax':'None'}
    _DEFAULT_SHAKE_BC = {'XMin':'Free-field',
                         'XMax':'Free-field',
                         'YMin':'Compliant base ',
                         'YMax':'None'}

    def __init__(self, s_i, g_i, g_o, b, d, soil, footing, column,
                 model_type='axisymmetry',  element_type='15-Noded', title='',
                 comments='', dstrata=None, wt=None, fill_angle=None, bfill=0.5,
                 nfill=None, dfill=None, interface=False, model_width=None,
                 model_depth=None, fill=None, mesh_density=0.06, 
                 dratchetting=0, ratchetting_material=None, 
                 ratchetting_threshold=np.inf,
                 locations=[0, 0.25, 0.5, 0.75, 1], build=True, excavation=True,
                 deformation_boundary_condition=None,
                 dynamic_boundary_condtions=None, 
                 shake_boundary_condtions=None, boundary_interface=False):
        """Initialize a new instance of `SymmetricPlateModel`.

        Parameters
        ----------
        s_i : Server
            Plaxis Input Application remote sripting server.
        g_i : PlxProxyGlobalObject
            Global object of the current open Plaxis model in Input.
        g_o : PlxProxyGlobalObject
            Global object of the current open Plaxis model in Output.
        b : float
            Foundation width [m].
        d : float
            Foundation depth [m].
        soil : soil : dict, list
            Dictionary with the material properties or list of
            dictionaries.
        footing : dict
            Dictionary with the properties of the material used in 
            the footing.
        column : dict, None
            Dictionary with the properties of the material used in 
            the footing. For surface foundaitons None.
        model_type : str, optional
            Model type: 'axisymmetry' or 'planestrain'. By default
            'axisymetry'. By dafault 'axisymmetry'.
        element_type : str, optional
            Element type: '6-Noded' or '15-Noded'. By default
            '15-Noded'.
        title : str, optional
            Model title in Plaxis. By default ''.
        comments : str, optional
            Model comments in Plaxis. By defautl ''.
        dstrata : list, None, optional
            Width of soil layers [m]. By defautl None.
        wt : float, None, optional
            Water tabe depth [m]. By default None.
        fill_angle : float, None, optional
            Fill angle [deg]. By default None.
        bfill : float, optional.
            Distance between foundation edge and the start of the fill
            slope [m]. By default 0.5.
        nfill : int, None, optional
            Number of fill layers. By default None.
        dfill : list, None, optional
            (nfill,) width of fill layers [m]. By default None.
        interface : bool, dict, optional
            Bool activates/deactivates all the interfaces. Otherwise a 
            dictionary with the 'top', 'bottom', 'column' and 'lateral'
            keys can be provided. For each key either a bool is provided
            indicating whether that interface will be considered in the
            model. Also a dict can be provided for each key with the
            soil material to be assigned to it. By default False.
        model_widht : float, None, optional
            User specified model width [m]. By default None.
        model_depth : float, None, optional
            User specified model depth [m]. By default None.
        fill : dict, list, None, optional
            Dictionary with the fill properties or list of dictionaries.
            By default None.
        mesh_density : float, optional
            Mesh density. By default 0.06.
        dratchetting : float, optional
            Widht of soil under the foundation that is replaced when
            ratchetting occurs [m]. By default 0.
        ratchetting_material  : dict, None, optional
            Dictionary with the material properties after ratchetting.
        ratchetting_threshold : float, optional
            Upwards displacement threshold that when surpassed by any
            output location under the foundation the material under
            it is replaced by the ratchetting material. By default
            np.inf.
        locations : array-like, optional
            (nloc, 1) location of output points in the foundation
            bottom, measured as [0, 1] where 0 is the center of the
            foundation and 1 the edge. By default
            [0, 0.25, 0.5, 0.75, 1].
        build : bool, optional
            Builds Plaxis model automatically. By default True.
        excavation : bool, optional
            If True in models with fill, the excavation and fill
            processes are included in the initial phases. By default
            True.
        deformation_boundary_condition : dict, None, optional
            Deformation boundary conditions of the model. If None the
            default setting is adopted. Dictionary with keys `XMin`,
            `XMax`, `YMin` and `YMax`, with supported values
            'Free',  'Normally fixed',  'Horizontally fixed',
            'Vertically fixed' and 'Fully fixed'. By default None.
        dynamic_boundary_condtions : dict, None, optional
            Dynamic boundary conditions of the model used in dynamic load
            tests. If None the default setting is adopted. Dictionary
            with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
            values 'None' and 'Viscous'. By default None.
        shake_boundary_condtions : dict, None, optional
            Dynamic boundary conditions of the model used in base shake
            tests. If None the default setting is adopted. Dictionary
            with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
            values 'None', 'Viscous', 'Free-field' and 'Compliant base'.
            By default None.
        boundary_interface : bool, optional
            Include boundary interfaces needed for a base shake test.
            This requires a much denser mesh and more computationally
            demanding models. By default False.
        """
        
        SG.__init__(self, b, d, dstrata=dstrata, wt=wt,
                    fill_angle=fill_angle, bfill=bfill, nfill=nfill,
                    dfill=dfill, dratchetting=dratchetting,
                    interface=interface, model_width=model_width,
                    model_depth=model_depth)
        PlateModel.__init__(self)
        Model.__init__(self, s_i, g_i, g_o, model_type, element_type, title,
                       comments, soil, fill, ratchetting_material,
                       ratchetting_threshold, mesh_density, locations,
                       excavation,
                       deformation_boundary_condition=deformation_boundary_condition,
                       dynamic_boundary_condtions=dynamic_boundary_condtions,
                       shake_boundary_condtions=shake_boundary_condtions,
                       boundary_interface=boundary_interface)
        self._init_foundation_material(footing, column)
        if build:
            self.build()


class NonSymmetricPlateModel(NSG, PlateModel, Model):
    """Shallow symmetric foundaiton Plaxis model with plate elements for
    the structure.

    Parameters
    ----------
    s_i : Server
        Plaxis Input Application remote sripting server.
    g_i : PlxProxyGlobalObject
        Global object of the current open Plaxis model in Input.
    g_o : PlxProxyGlobalObject
        Global object of the current open Plaxis model in Output.
    b : float
        Foundation width [m].
    d : float
        Foundation depth [m].
    soil : soil : dict, list
        Dictionary with the material properties or list of
        dictionaries.
    footing : dict
        Dictionary with the properties of the material used in 
        the footing.
    column : dict, None
        Dictionary with the properties of the material used in 
        the footing. For surface foundaitons None.
    b2 : float, None, optional.
        Distance from the left edge of the footing to the center of
        the column [m] (0<=b2<=b). If None then b/2. By default
        None.
    model_type : str, optional
        Model type: 'axisymmetry' or 'planestrain'. By default
        'axisymetry'. By dafault 'planestrain'.
    element_type : str, optional
        Element type: '6-Noded' or '15-Noded'. By default '15-Noded'.
    title : str, optional
        Model title in Plaxis. By default ''.
    comments : str, optional
        Model comments in Plaxis. By defautl ''.
    dstrata : list, None, optional
        Width of soil layers [m]. By defautl None.
    wt : float, None, optional
        Water tabe depth [m]. By default None.
    fill_angle : float, None, optional
        Fill angle [deg]. By default None.
    bfill : float, optional.
        Distance between foundation edge and the start of the fill
        slope [m]. By default 0.5.
    nfill : int, None, optional
        Number of fill layers. By default None.
    dfill : list, None, optional
        (nfill,) width of fill layers [m]. By default None.
    interface : bool, dict, optional
        Bool activates/deactivates all the interfaces. Otherwise a 
        dictionary with the 'top', 'bottom', 'column' and 'lateral'
        keys can be provided. For each key either a bool is provided
        indicating whether that interface will be considered in the
        model. Also a dict can be provided for each key with the
        soil material to be assigned to it. By default False.
    model_widht : float, None, optional
        User specified model width [m]. By default None.
    model_depth : float, None, optional
        User specified model depth [m]. By default None.
    fill : dict, list, None, optional
        Dictionary with the fill properties or list of dictionaries.
        By default None.
    mesh_density : float, optional
        Mesh density. By default 0.06.
    dratchetting : float, optional
        Widht of soil under the foundation that is replaced when
        ratchetting occurs [m]. By default 0.
    ratchetting_material  : dict, None, optional
        Dictionary with the material properties after ratchetting.
    ratchetting_threshold : float, optional
        Upwards displacement threshold that when surpassed by any
        output location under the foundation the material under
        it is replaced by the ratchetting material. By default
        np.inf.
    locations : array-like, optional
        (nloc, 1) location of output points in the foundation
        bottom, measured as [0, 1] where 0 is the center of the
        foundation and 1 the edge. By default
        [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1].
    build : bool, optional
        Builds Plaxis model automatically. By default True.
    excavation : bool, optional
        If True in models with fill, the excavation and fill
        processes are included in the initial phases. By default
        True.
    deformation_boundary_condition : dict, None, optional
        Deformation boundary conditions of the model. If None the
        default setting is adopted. Dictionary with keys `XMin`,
        `XMax`, `YMin` and `YMax`, with supported values
        'Free',  'Normally fixed',  'Horizontally fixed',
        'Vertically fixed' and 'Fully fixed'. By default None.
    dynamic_boundary_condtions : dict, None, optional
        Dynamic boundary conditions of the model used in dynamic load
        tests. If None the default setting is adopted. Dictionary
        with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
        values 'None' and 'Viscous'. By default None.
    shake_boundary_condtions : dict, None, optional
        Dynamic boundary conditions of the model used in base shake
        tests. If None the default setting is adopted. Dictionary
        with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
        values 'None', 'Viscous', 'Free-field' and 'Compliant base'.
        By default None.
    boundary_interface : bool, optional
        Include boundary interfaces needed for a base shake test.
        This requires a much denser mesh and more computationally
        demanding models. By default False.
    
    Methods
    -------
    build()
        Builds the model in Plaxis.
    regen(s_i, g_i, g_o, test=False) : 
        Regenerates the model in Plaxis. Optinoally it recalculates
        previous load tests.
    save(filename)
        Saves model to file. Plaxis objects cannot be stored, only
        input properties and results. When loaded, the model can
        be regenerated with <regen> method.
    load(filename)
        Loads saved test.
    failure_test(testid, load, max_load=[np.inf, np.inf, np.inf], load_factor=2, load_increment=[0, 0, 0], qsurf=None, start_from='construction', delete_fail=True)
        Test the foundation until the model does not converge.
    load_test(testid, load, start_from='construction', qsurf=None, delete_fail=True)
        Conducts a load test in the model.
    safety_test(testid, start_from, test='incremental', SumMsf=None, Msf=0.1, qsurf=None, delete_fail=True)
        Conducts a safety test on the model.
    dynamic_test(testid, time, load, start_from='construction', nsubstep=10, qsurf=None, delete_fail=True)
        Apply a dynamic load to the foundation.
    shake_test(testid, time, acceleration, start_from='construction', qsurf=None, nsubstep=10, delete_fail=True)
        Apply a displacement time history at the model base.
    delete_test( testid, delete_phases=True) 
        Deletes a test from the model.
    plot(figsize=2.5, foundation=True, fill=True, soil=True, excavation=False, ratchetting=True, wt=True, interface=False, output_location=False)
        Foundation plot.
    plot_test(testid, force=None, displacement=None, phase=None, location=None, compression_positive=True, pullout_positive=False, reset_start=False, legend=False, xlim=None, ylim=None, figsize=(4, 3))
        Plots test results.
    plot_safety_test(testid, location=None, pullout_positive=False, reset_start=False, legend=False, figsize=(6, 4))
        Plots safety test.
    plot_dynamic_test(testid, displacement=None, force=None, location=None, compression_positive=True, pullout_positive=False, xlim=None, ylim=None, legend=False, figsize=(8, 2))
        Plot dynamic test resutls versus time.
    plot_shake_test(self, testid, displacement=None, acceleration=None, location=None, pullout_positive=False, xlim=None, ylim=None, legend=False, figsize=(8, 2))
        Plot shake test results versus time.
    """

    _DEFAULT_DEFORMATION_BC = {'XMin':'Horizontally fixed',
                               'XMax':'Horizontally fixed',
                               'YMin':'Fully fixed',
                               'YMax':'Free'}
    _DEFAULT_DYNAMIC_BC = {'XMin':'Viscous',
                           'XMax':'Viscous',
                           'YMin':'Viscous',
                           'YMax':'None'}
    _DEFAULT_SHAKE_BC = {'XMin':'Free-field',
                         'XMax':'Free-field',
                         'YMin':'Compliant base ',
                         'YMax':'None'}

    def __init__(self, s_i, g_i, g_o, b, d, soil, footing, column, b2=None,
                 model_type='planestrain',  element_type='15-Noded', title='',
                 comments='', dstrata=None, wt=None, fill_angle=None, bfill=0.5,
                 nfill=None, dfill=None, interface=False, model_width=None,
                 model_depth=None, fill=None, mesh_density=0.06, 
                 dratchetting=0, ratchetting_material=None, 
                 ratchetting_threshold=np.inf,
                 locations=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],
                 build=True, excavation=True,
                 deformation_boundary_condition=None,
                 dynamic_boundary_condtions=None, shake_boundary_condtions=None,
                 boundary_interface=False):
        """Initialize a new instance of `NonSymmetricPlateModel`.

        Parameters
        ----------
        s_i : Server
            Plaxis Input Application remote sripting server.
        g_i : PlxProxyGlobalObject
            Global object of the current open Plaxis model in Input.
        g_o : PlxProxyGlobalObject
            Global object of the current open Plaxis model in Output.
        b : float
            Foundation width [m].
        d : float
            Foundation depth [m].
        soil : soil : dict, list
            Dictionary with the material properties or list of
            dictionaries.
        footing : dict
            Dictionary with the properties of the material used in 
            the footing.
        column : dict, None
            Dictionary with the properties of the material used in 
            the footing. For surface foundaitons None.
        b2 : float, None, optional.
            Distance from the left edge of the footing to the center of
            the column [m] (0<=b2<=b). If None then b/2. By default
            None.
        model_type : str, optional
            Model type: 'axisymmetry' or 'planestrain'. By default
            'axisymetry'. By dafault 'planestrain'.
        element_type : str, optional
            Element type: '6-Noded' or '15-Noded'. By default
            '15-Noded'.
        title : str, optional
            Model title in Plaxis. By default ''.
        comments : str, optional
            Model comments in Plaxis. By defautl ''.
        dstrata : list, None, optional
            Width of soil layers [m]. By defautl None.
        wt : float, None, optional
            Water tabe depth [m]. By default None.
        fill_angle : float, None, optional
            Fill angle [deg]. By default None.
        bfill : float, optional.
            Distance between foundation edge and the start of the fill
            slope [m]. By default 0.5.
        nfill : int, None, optional
            Number of fill layers. By default None.
        dfill : list, None, optional
            (nfill,) width of fill layers [m]. By default None.
        interface : bool, dict, optional
            Bool activates/deactivates all the interfaces. Otherwise a 
            dictionary with the 'top', 'bottom', 'column' and 'lateral'
            keys can be provided. For each key either a bool is provided
            indicating whether that interface will be considered in the
            model. Also a dict can be provided for each key with the
            soil material to be assigned to it. By default False.
        model_widht : float, None, optional
            User specified model width [m]. By default None.
        model_depth : float, None, optional
            User specified model depth [m]. By default None.
        fill : dict, list, None, optional
            Dictionary with the fill properties or list of dictionaries.
            By default None.
        mesh_density : float, optional
            Mesh density. By default 0.06.
        dratchetting : float, optional
            Widht of soil under the foundation that is replaced when
            ratchetting occurs [m]. By default 0.
        ratchetting_material  : dict, None, optional
            Dictionary with the material properties after ratchetting.
        ratchetting_threshold : float, optional
            Upwards displacement threshold that when surpassed by any
            output location under the foundation the material under
            it is replaced by the ratchetting material. By default
            np.inf.
        locations : array-like, optional
            (nloc, 1) location of output points in the foundation
            bottom, measured as [0, 1] where 0 is the center of the
            foundation and 1 the edge. By default
            [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1].
        build : bool, optional
            Builds Plaxis model automatically. By default True.
        excavation : bool, optional
            If True in models with fill, the excavation and fill
            processes are included in the initial phases. By default
            True.
        deformation_boundary_condition : dict, None, optional
            Deformation boundary conditions of the model. If None the
            default setting is adopted. Dictionary with keys `XMin`,
            `XMax`, `YMin` and `YMax`, with supported values
            'Free',  'Normally fixed',  'Horizontally fixed',
            'Vertically fixed' and 'Fully fixed'. By default None.
        dynamic_boundary_condtions : dict, None, optional
            Dynamic boundary conditions of the model used in dynamic load
            tests. If None the default setting is adopted. Dictionary
            with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
            values 'None' and 'Viscous'. By default None.
        shake_boundary_condtions : dict, None, optional
            Dynamic boundary conditions of the model used in base shake
            tests. If None the default setting is adopted. Dictionary
            with keys `XMin`, `XMax`, `YMin` and `YMax`, with supported
            values 'None', 'Viscous', 'Free-field' and 'Compliant base'.
            By default None.
        boundary_interface : bool, optional
            Include boundary interfaces needed for a base shake test.
            This requires a much denser mesh and more computationally
            demanding models. By default False.
        """
        
        NSG.__init__(self, b, d, b2=b2, dstrata=dstrata, wt=wt,
                     fill_angle=fill_angle, bfill=bfill, nfill=nfill,
                     dfill=dfill, dratchetting=dratchetting,
                     interface=interface, model_width=model_width,
                     model_depth=model_depth)
        PlateModel.__init__(self)
        Model.__init__(self, s_i, g_i, g_o, model_type, element_type, title,
                       comments, soil, fill, ratchetting_material,
                       ratchetting_threshold, mesh_density, locations,
                       excavation,
                       deformation_boundary_condition=deformation_boundary_condition,
                       dynamic_boundary_condtions=dynamic_boundary_condtions,
                       shake_boundary_condtions=shake_boundary_condtions,
                       boundary_interface=boundary_interface)
        self._init_foundation_material(footing, column)
        if build:
            self.build()
        