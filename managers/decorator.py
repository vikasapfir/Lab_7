import logging

def logged(exception,mode):
  def decorator(func):
    def wrapper(*args, **kwargs):
      
        try:
          return func(*args, **kwargs)
        except exception as e:
          if mode == 'console':
            logging.error(f"Exception: {e}")
          elif mode == 'file':
            logging.basicConfig(filename="log.log",level=logging.ERROR,format='%(asctime)s %(levelname)s %(message)s', datefmt="%Y-%m-%d %I:%M:%S%p",)
            logging.error(f"Exception: {e}")
          else:
            raise ValueError("Invalid mode value!")
            
    return wrapper
  return decorator

