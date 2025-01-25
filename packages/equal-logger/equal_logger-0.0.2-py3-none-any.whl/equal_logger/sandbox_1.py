from logger import Logger

logger = Logger(
    cloud="AZURE",
    script_name="sandbox_1.py",
    data_source="Testando",
    project="comodo",
    credentials=r"C:\Users\gustavo\Desktop\equal-logger\src\equal_logger\cred_azure.json" #teste no pc do gus
)

logger.success("titulo 1", "descricao 1", print_log=False)
logger.info("titulo 1", "descricao 1", print_log=False)
logger.error("titulo 1", "descricao 1", print_log=False)

logger.save()