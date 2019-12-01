import os

path = os.path.dirname(os.path.abspath(__file__))
# print(path)
f = open(os.path.join(path,'input.txt'), 'r')
modules = f.read()
modules_masses = [int(x) for x in modules.split()]
print(modules_masses)

def get_necessary_fuel(mass):
    return int(mass/3)-2


fuel_need_per_module=[]
for module in modules_masses:
    print('Module ', module, ':')
    f = get_necessary_fuel(module)
    total_fuel_per_module=f
    while f>0:
        # print(f)
        f = get_necessary_fuel(f)
        if f<0:
            continue
        total_fuel_per_module+=f   
    fuel_need_per_module.append(total_fuel_per_module)
    print('Total Fuel for module {mod} is {fuel}'.format(mod=str(module), fuel=str(total_fuel_per_module)))
        
total_fuel_needed=sum(fuel_need_per_module)
print('Absolute total fuel needed', str(total_fuel_needed))


