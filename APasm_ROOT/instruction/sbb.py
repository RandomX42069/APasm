import importlib.util as im

# Import RM dynamically
rmpath = "APasm_ROOT/definitions/RM.py"
rmspec = im.spec_from_file_location("rmmodule", rmpath)
rmmodule = im.module_from_spec(rmspec)
rmspec.loader.exec_module(rmmodule)

modpath = "APasm_ROOT/definitions/mod.py"
modspec = im.spec_from_file_location("modmodule", modpath)
modmodule = im.module_from_spec(modspec)
modspec.loader.exec_module(modmodule)

modrmpath = "APasm_ROOT/definitions/modrm.py"
modrmspec = im.spec_from_file_location("modrmmodule", modrmpath)
modrmmodule = im.module_from_spec(modrmspec)
modrmspec.loader.exec_module(modrmmodule)

movpath = "APasm_ROOT/instruction/mov.py"
movspec = im.spec_from_file_location("movmodule", movpath)
movmodule = im.module_from_spec(movspec)
movspec.loader.exec_module(movmodule)

