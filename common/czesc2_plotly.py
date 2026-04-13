# Zadanie 4 Plotly

# Stwórz wykres punktowy, który pokaże zależność między:
# - liczbą godzin nauki
# - wynikiem egzaminu
# import plotly.express as px
# godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
# wyniki = [40, 50, 55, 60, 70, 75, 85]
#
# fig = px.scatter(x=godziny_nauki,
#                  y=wyniki,
#                  title="liczba godz nauki vs wynik egz",
#                  labels={"x":"godziny nauli", "y": "wyniki"}, text=wyniki)
# fig.update_traces(
#     textposition="top center",
#     marker=dict(size=4, color="red"),
# textfont=dict(size=10)
# )
# fig.show()

# --------------------------------------------------------------
# Zadanie 5 Plotly
# Stwórz wykres kołowy, który pokaże udział języków programowania używanych przez programistów w projekcie.
# import plotly.express as px
# jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
# udzial = [35, 30, 15, 10, 10]
# fig = px.pie(names=jezyki, values=udzial, title="Udzial",
# labels={"names": "Język", "values": "Udział (%)"}
# )
#
# fig.update_traces(
#     textinfo="label+percent",
#     textfont_size=6,
#     pull=[0.05, 0, 0, 0, 0])   # lekko wysunięty Python
# fig.show()
# #
# ------------------------------------------------------------------------------
# Zadanie 6 Plotly
# Stwórzinteraktywny wykres liniowy, który pokaże temperaturę w kolejnych dniach tygodnia.
import plotly.express as px
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]
fig=px.line(x=dni,
            y=temperatura,
            title='Temperatura',
            labels={'x': 'dzien tyg', 'y': 'temperatura'},
            text = temperatura,)
fig.update_traces(
    textposition="top center",
    textfont=dict(size=5),        # wielkość podpisów
    marker=dict(size=6, color="red")  # wygląd punktów
)
fig.show()