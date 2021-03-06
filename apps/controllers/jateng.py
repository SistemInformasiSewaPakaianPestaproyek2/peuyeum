import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,keyuri,setTTL
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jateng'
		listkabkot = [
		'%3301%','%3302%','%3303%','%3304%','%3305%','%3306%','%3307%','%3308%','%3309%','%3310%',
		'%3311%','%3312%','%3313%','%3314%','%3315%','%3316%','%3317%','%3318%','%3319%','%3320%',
		'%3321%','%3322%','%3323%','%3324%','%3325%','%3326%','%3327%','%3328%','%3329%',
		'%3371%','%3372%','%3373%','%3374%','%3375%','%3376%','%3388','$3399','%3579','%3578','%3577'
		]
		provloc = '110.159872, -7.138075'
		mapzoom = '9'
		kabkotcord = [
		'109.022556, -7.700959',
		'9.099209, -7.412765',
		'109.360424, -7.386681',
		'109.540683, -7.446158',
		'109.660262, -7.671469',
		'110.009113, -7.713267',
		'109.897408, -7.370507', #RF
		'110.206305, -7.480867',
		'110.59148, -7.523172',
		'110.664080, -7.739502',
		'110.820435, -7.684186',
		'110.925449, -7.790413',
		'110.984578, -7.607561',
		'111.025518, -7.418141',
		'110.838309, -7.069161',
		'111.411095, -6.968463',
		'111.331837, -6.707997',
		'111.035644, -6.749004',#ali
		'110.874834, -6.768993',#ali
		'110.791058, -6.582443',#ali
		'110.636269, -6.895762',#ali
		'110.428458, -6.999214',#ali
		'110.117773, -7.239196',#ali
		'110.155868, -6.984265',#ali
		'109.866806, -7.015625',#ali
		'109.673988, -6.891339',#ali
		'109.392345, -7.021363',#ali
		'109.123720, -6.878921',#uki
		'108.884346, -7.013345',#uki
		'110.223011, -7.481218',#uki
		'110.823955, -7.574859',#uki
		'110.503626, -7.331238',#uki
		'110.429121, -7.001583',#uki
		'109.673467, -6.889120',#uki
		'109.101790, -6.861921',#uki
		'109.485088, -7.560118',#uki
		'110.354836, -7.168365',#uki
        '112.534161 -7.881966',
        '112.745670 -7.257927',
        '111.527879 -7.630911',
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		return dt