import matplotlib.pyplot as plt
height=[5.1,5.5,6.0,5.0,6.3]
names=('Asma','Bela','Cris','Diya','Sakib')
plt.barh(names,height)
plt.xlabel("Height")
plt.ylabel("Names")
plt.show()
