import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from get_data import getRepositories
from get_data import showKeys
from get_data import viewInformation
from save_results import saveToPDF


def topProjectStatistic():
    url = 'https://api.github.com/search/repositories?q=stars:%3E=10&sort=starts'
    response_dict = getRepositories(url)
    repo_dicts = response_dict['items']
    print("Liczba zwróconych repozytoriów: ", len(repo_dicts))
    showKeys(repo_dicts)
    print("Najbardziej popularne repozytoria na GitHubie to: \n")
    viewInformation(repo_dicts)

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


def viewBrowserTopProjectStats():

    names, stars = topProjectStatistic()
    my_style = LS('#53A0E8', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Topowe projekty na GitHubie wedlug liczby gwiazdek'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('top_projects.svg')
    chart.render_in_browser()


def savePDFTopProjectStats():

    names, stars = topProjectStatistic()
    my_style = LS('#53A0E8', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Topowe projekty na GitHubie wedlug liczby gwiazdek'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('top_projects.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//top_projects.svg'
    name = "C://Users//domin//Downloads//top_projects.pdf"
    saveToPDF(svgFile, name)
