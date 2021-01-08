import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from get_data import getRepositories
from save_results import saveToPDF


def pythonStarStatistic():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response_dict = getRepositories(url)
    repo_dicts = response_dict['items']
    print("Liczba zwróconych repozytoriów: ", len(repo_dicts))

    names, stars = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label:': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
        stars.append(plot_dict)

    return names, stars


def viewBrowserPythonStats():

    names, stars = pythonStarStatistic()
    my_style = LS('#333398', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    chart = pygal.Bar(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Oznaczone najwiekszą liczbą gwiazdek projekty Pythona w serwisie GitHub'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_in_browser()


def savePDFPythonStats():
    names, stars = pythonStarStatistic()
    my_style = LS('#333398', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    chart = pygal.Bar(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Oznaczone najwiekszą liczbą gwiazdek projekty Pythona w serwisie GitHub'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('python_repos.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//python_repos.svg'
    name = "C://Users//domin//Downloads//Python_repos.pdf"
    saveToPDF(svgFile, name)
