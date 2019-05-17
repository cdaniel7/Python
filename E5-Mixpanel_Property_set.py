from mixpanel_api import Mixpanel


if __name__ == '__main__':

	api_secret = 'XXX'
	project_token = 'YY'
	
	m = Mixpanel(api_secret,token=project_token, pool_size=4, timeout=60*60, debug=True) 

        m.import_people('data.csv',ignore_alias=False,dataset_version=None,raw_record_import=False)
        
        

