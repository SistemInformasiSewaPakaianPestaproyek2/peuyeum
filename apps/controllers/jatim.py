import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		kabkotcord = [
		'111.105904, -8.180052',
		'111.459364, -7.938566',
		'111.592798, -8.157817',
		'111.955060, -8.090436',
		'112.166403, -8.094802',
		'112.016871, -7.846838',
		'112.639219, -7.971031',
		'113.227336, -8.134823',
		'113.664399, -8.200297',
		'114.317427, -8.220783',
		'113.823270, -7.918907',
		'113.995393, -7.705290',
		'113.203210, -7.771583',
		'112.897102, -7.647793',
		'112.703775, -7.449440',
		'112.430201, -7.472955',
		'112.260553, -7.538246',
		'111.895033, -7.605524',
		'111.534682, -7.632213',
		'111.336947, -7.649282',
		'111.276713, -7.437916',
		'111.778154, -7.267259',
		'111.897522, -6.933019',
		'112.620912, -7.12159',
		'112.652396, -7.161469',
		'112.75679, -7.026468',
		'113.258399, -7.189547',
		'113.473311, -7.150556',
		'113.878849, -7.020012',
		'112.016871, -7.850579', #71
		'112.161994, -8.096183',
		'112.638303, -7.965719',
		'113.201292, -7.776733',
		'112.899773, -7.646969',
		'112.439574, -7.470467',
		'111.530797, -7.630911',
		'112.752537, -7.254862',
		'112.53329, -7.882909'
		]
		listkabkot = [
		'%3501%','%3502%','%3503%','%3504%','%3505%','%3506%','%3507%','%3508%','%3509%','%3510%',
		'%3511%','%3512%','%3513%','%3514%','%3515%','%3516%','%3517%','%3518%','%3519%','%3520%',
		'%3521%','%3522%','%3523%','%3524%','%3525%','%3526%','%3527%','%3528%','%3529%',
		'%3571%','%3572%','%3573%','%3574%','%3575%','%3576%','%3577%','%3578%','%3579%'
		]
		provinsi = 'jatim'
		provloc = '112.351224, -7.698205'
		mapzoom = '9'
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