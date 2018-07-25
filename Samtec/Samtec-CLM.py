from KicadModTree import *
from KicadModTree.nodes.specialized.PadArray import PadArray

for numpos in range(2, 50):
    footprint_name = "CLM-1%02d-02-F-D" % numpos
    
    # init kicad footprint
    kicad_mod = Footprint(footprint_name)
    kicad_mod.setDescription("1.00 mm Tiger Claw(TM) Rugged Reliable Dual Wipe")
    kicad_mod.setTags("Samtec " + footprint_name)
    
    # set general values
    kicad_mod.append(Text(type='reference', text='REF**', at=[0, -3], layer='F.SilkS'))
    kicad_mod.append(Text(type='value', text=footprint_name, at=[1.5, 3], layer='F.Fab'))
    
    # create silscreen
    kicad_mod.append(RectLine(start=[-numpos/2, -1.27], end=[numpos/2, 1.27], layer='F.SilkS'))
    
    # create courtyard
    kicad_mod.append(RectLine(start=[-numpos/2, -2.286], end=[numpos/2, 2.286], layer='F.CrtYd'))
    
    # create pad    
    kicad_mod.append(PadArray(pincount=numpos,spacing=[1,0],center=[0,-1.6], initial=1, increment=2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, size=[0.61,1.37], layers=Pad.LAYERS_SMT))
    kicad_mod.append(PadArray(pincount=numpos,spacing=[1,0],center=[0,1.6], initial=2, increment=2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, size=[0.61,1.37], layers=Pad.LAYERS_SMT))

    kicad_mod.append(Pad(number ='""', type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                         at=[-numpos/2+1, 0],
                         size=0.635, drill=0.635,
                         layers=Pad.LAYERS_NPTH))
    kicad_mod.append(Pad(number ='""', type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                         at=[numpos/2-1, 0],
                         size=0.635, drill=0.635,
                         layers=Pad.LAYERS_NPTH))
    
    # add model
    kicad_mod.append(Model(filename="${KISYS3DMOD}/Connector_Samtec_CLM.3dshapes/" + footprint_name.upper() + ".stp",
                               at=[0, 0, 0], scale=[1, 1, 1], rotate=[-90, 0, 0]))
    
    # output kicad model
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile(footprint_name + '.kicad_mod')

