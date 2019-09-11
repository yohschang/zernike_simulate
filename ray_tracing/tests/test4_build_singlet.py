
import lens, trace, cal_tools
import matplotlib.pyplot as __plt__
New_Lens = lens.Lens(lens_name='singlet',creator='XF')
New_Lens.add_surface(number=1,radius=10000000,thickness=10,glass='air')
New_Lens.add_surface(number=2,radius=50,thickness=5,glass='BK7_SCHOTT',STO=True)
New_Lens.add_surface(number=3,radius=1175.71,thickness=96.672,s='air')
New_Lens.add_surface(number=4,radius=10000000,thickness=0,s='air')

New_Lens.lens_info()

New_Lens.add_field(angle=0)
print '-------------------------------------------------------'
ray_list = trace.trace_sys(New_Lens)

x2 = []
y2 = []
z2 = []

for ray in ray_list:
	x2.append(ray.Pos[0])
	y2.append(ray.Pos[1])
	z2.append(ray.Pos[2])

fig = __plt__.figure()
__plt__.plot(x2,y2,'bo')
__plt__.show()

rms = cal_tools.rms(ray_list)
print rms

#New_Lens.list_surface()
# surface.add(I,)	

# New_Rays = ray.Ray()

# field.add()
# field.add()
# field.add()

# trace.tracing(New_Lens,New_Rays,I)
	