class Config:
	DEBUG = True
	FLASK_RUN_HOST = 'localhost'
	FLASK_RUN_PORT = 5000
	SUPPORTED_IMAGES_EXT = ['image/png', 'image/jpeg, image/jpg']
	FILE_ALLOWED = SUPPORTED_IMAGES_EXT
	SECRET_KEY = '86a4e665edf6b9ca42924fd7b97b8ada'