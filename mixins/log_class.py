from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:

    def _log(self, msg):
        raise NotImplementedError('Method log not implemented')

    def log_error(self, msg):
        return self._log(f'[ERROR] {msg}')

    def log_suceess(self, msg):
        return self._log(f'[SUCCESS] {msg}')


class LogFileMixin(Log):

    def _log(self, msg):
        with open(LOG_FILE, 'a') as f:
            f.write(f'{msg}\n')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f' {msg}, ({self.__class__.__name__})  ')


if __name__ == '__main__':
    log_file = LogFileMixin()
    log_print = LogPrintMixin()
    log_file.log_error('Hello, World!')
    log_file.log_suceess('Hello, World!')
    log_print.log_suceess('Hello, World!')
