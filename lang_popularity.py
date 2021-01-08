import pandas as pd
import pygal
from get_data import getRepositories
from save_results import saveToPDF


def languageStatistic():
    url = 'https://api.github.com/search/repositories?per_page=100&q=followers:%3E=1000&sort=stars'
    response_dict = getRepositories(url)
    repo_dicts = response_dict['items']
    print("Liczba zwróconych repozytoriów: ", len(repo_dicts))

    languages = []
    dates = []
    for repo_dict in repo_dicts:
        if repo_dict['language'] and repo_dict['created_at']:
            languages.append(repo_dict['language'].strip())
            dates.append(repo_dict['created_at'])

    no_of_projects = len(languages)
    data = {'Language': languages, 'Date_time': dates}
    df = pd.DataFrame(data)

    for i,__ in enumerate(df['Date_time']):
        date = df['Date_time'].iloc[i]
        date= date[0:4]
        df['Date_time'].iloc[i] = date

    gr = df.groupby(df.columns.tolist(), as_index=False).size()
    print(gr)

    year_start = int(str(min(df['Date_time']))[0:4])
    year_end = int(str(max(df['Date_time']))[0:4])
    years_list = [(i) for i in range(year_start, year_end + 1)]

    dane = {'Language': df['Language'].unique()}
    for year in years_list:
        dane[year] = [(0) for i in range(len(df['Language'].unique()))]
    result = pd.DataFrame(dane)
    for i,__ in enumerate(gr["Date_time"]):
        for year in years_list:
            if str(year) == gr['Date_time'].iloc[i]:
                language = gr['Language'].iloc[i]
                for j,lang in enumerate(df['Language'].unique()):
                    if lang == language:
                        result[year].iloc[j] = gr["size"].iloc[i]

    return result, years_list, no_of_projects


def view_line():
    result, years, __ = languageStatistic()

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    line_chart = pygal.Line(my_config)
    line_chart.title = 'Timeline analysis'
    line_chart.force_uri_protocol = 'http'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end+1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_in_browser()


def savePDF_line():

    result, years, __ = languageStatistic()
    line_chart = pygal.Line()
    line_chart.title = 'Timeline analysis'
    line_chart.force_uri_protocol = 'http'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end + 1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_to_file('timeline.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//timeline.svg'
    name = "C://Users//domin//Downloads//timeline_chart.pdf"
    saveToPDF(svgFile, name)


def view_bar_stacked():
    result, years, no_of_projects = languageStatistic()

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    result.loc[:, result.columns != 'Language'] = (result.loc[:, result.columns != 'Language'] / result.loc[:, result.columns != 'Language'].sum()) * 100

    line_chart = pygal.StackedBar(my_config)
    line_chart.title = 'Timeline analysis'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end+1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_in_browser()
    line_chart.render_to_file('timeline_bar_stacked.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//timeline_bar_stacked.svg'
    name = "C://Users//domin//Downloads//timeline_bar_stacked.pdf"
    saveToPDF(svgFile, name)


def savePDF_bar_stacked():
    result, years, no_of_projects = languageStatistic()

    result.loc[:, result.columns != 'Language'] = (result.loc[:, result.columns != 'Language'] / result.loc[:,result.columns != 'Language'].sum()) * 100

    line_chart = pygal.StackedBar()
    line_chart.title = 'Timeline analysis'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end + 1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_to_file('timeline_bar_stacked.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//timeline_bar_stacked.svg'
    name = "C://Users//domin//Downloads//timeline_bar_stacked.pdf"
    saveToPDF(svgFile, name)


def view_bar_horizontal():

    result, years, __ = languageStatistic()

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    line_chart = pygal.HorizontalBar(my_config)
    line_chart.title = 'Timeline analysis'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end+1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_in_browser()


def savePDF_bar_horizontal():

    result, years, __ = languageStatistic()
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Timeline analysis'
    year_start, year_end = min(years), max(years)
    line_chart.x_labels = map(str, range(year_start, year_end + 1))

    for i, lang in enumerate(result['Language']):
        cut_lang = result.loc[:, result.columns != 'Language']
        values_yearly = list(cut_lang.iloc[i])
        line_chart.add(lang, values_yearly)

    line_chart.render_to_file('timeline_bar_horizontal.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//timeline_bar_horizontal.svg'
    name = "C://Users//domin//Downloads//timeline_bar_horizontal.pdf"
    saveToPDF(svgFile, name)