import sys
import logging

def error_msg_details(err,err_detail:sys):
    _,_,exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_msg = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(err)
    )
    return err_msg


class CustomException(Exception):
    def __init__(self, err_msg,err_detail:sys):
        super().__init__(err_msg)
        self.err_msg = error_msg_details(err_msg,err_detail=err_detail)
    def __str__(self):
        return self.err_msg

# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero Error")
#         raise CustomException(e,sys)