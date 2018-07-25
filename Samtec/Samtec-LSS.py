from KicadModTree import *
from KicadModTree.nodes.specialized.PadArray import PadArray

for numpos in (10, 20, 30, 40, 50):
    for stackheight in ("01", "02"):
        padspacing = 0.635

        footprint_name = "LSS-1" + str(numpos) + "-" + stackheight + "-l-dv-a"

        # init kicad footprint
        kicad_mod = Footprint(footprint_name)
        kicad_mod.setDescription("0.635 mm Razor Beam(TM) High-Speed Hermaphroditic Terminal/Socket Strip")
        kicad_mod.setTags("Samtec " + footprint_name)
        
        # set general values
        kicad_mod.append(Text(type='reference', text='REF**', at=[0, -3], layer='F.SilkS'))
        kicad_mod.append(Text(type='value', text=footprint_name, at=[1.5, 3], layer='F.Fab'))
        
        # create silkscreen
        kicad_mod.append(RectLine(start=[-numpos*padspacing/2 - 2.375, -2], end=[numpos*padspacing/2 + 2.375, 2], layer='F.SilkS'))
        
        # create courtyard
        kicad_mod.append(RectLine(start=[-numpos*padspacing/2 - 2.375, -5.2/2], end=[numpos*padspacing/2 + 2.375, 5.2/2], layer='F.CrtYd'))
        
        padsize = [0.4, 1.6]
        padcenter = 1.8
        
        # create pad    
        kicad_mod.append(PadArray(pincount=numpos,spacing=[padspacing, 0],center=[0,-padcenter], initial=1, increment=2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, size=padsize, layers=Pad.LAYERS_SMT))
        kicad_mod.append(PadArray(pincount=numpos,spacing=[padspacing, 0],center=[0,padcenter], initial=2, increment=2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, size=padsize, layers=Pad.LAYERS_SMT))
        
        kicad_mod.append(Pad(number ='""', type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                             at=[-numpos*padspacing/2-1.5/2, -1.1],
                             size=0.89, drill=0.89,
                         layers=Pad.LAYERS_NPTH))
        kicad_mod.append(Pad(number ='""', type=Pad.TYPE_NPTH, shape=Pad.SHAPE_CIRCLE,
                             at=[numpos*padspacing/2+1.5/2, -1.1],
                             size=0.89, drill=0.89,
                         layers=Pad.LAYERS_NPTH))
    
        # add model
        kicad_mod.append(Model(filename="${KISYS3DMOD}/Connector_Samtec_LSS.3dshapes/" + footprint_name.upper() + "-TR.stp",
                               at=[0, 0, 0], scale=[1, 1, 1], rotate=[-90, 0, 0]))
        
        # output kicad model
        file_handler = KicadFileHandler(kicad_mod)
        file_handler.writeFile(footprint_name + '.kicad_mod')
