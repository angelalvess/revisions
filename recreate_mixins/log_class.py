from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('log method must be implemented')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):

        with open(LOG_FILE, 'a') as file:
            file.write(f'{msg}\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    logFile = LogFileMixin()
    logFile.log_error('Log File message')
    logPrint = LogPrintMixin()
    logPrint.log_error('Log Print message')
