import requests


class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'


def fetch_github(user):
    ''' Call to GitHub API '''
    URL = f'https://api.github.com/users/{user}/repos'
    req = requests.get(URL)
    return(req.json())

def fetch_github_repo(user, repo):
    ''' Call to GitHub API '''
    URL = f'https://api.github.com/repos/{user}/{repo}'
    req = requests.get(URL)
    return(req.json())

class CLI():
    ''' User interface '''

    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'\n{Format.BLUE}{Format.BOLD}Welcome{Format.CLEAR}\n')
        self.menu()

    def menu(self):
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(
                f'''\n{Format.BLUE}Please enter a github username\n{Format.CLEAR}''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            data_two = fetch_github(self._user_input)
            for x in data_two:
                print(f'{x["name"]}')
            self.get_repo_choice(self._user_input)
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def get_repo_choice(self, user):
        try:
            self._user_input = input(
                f'''\n{Format.BLUE}Please enter a repo name\n{Format.CLEAR}''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            data_three = fetch_github_repo(user, self._user_input)
            print(data_three)
            self.get_repo_choice(user)
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()
       

    def show_house(self):
        print(f'\tHello!')

    @staticmethod
    def valid_input(i):
        return True
    @staticmethod
    def goodbye():
        print(f'\n{Format.BLUE}{Format.BOLD}Goodbye!{Format.CLEAR}\n')

if __name__ == '__main__':
    app = CLI()
