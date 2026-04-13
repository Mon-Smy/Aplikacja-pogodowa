# Zadanie 1 Matplotlib
# Stwórz wykres liniowy, który pokaże sprzedaż sklepu w kolejnych dniach tygodnia.
# Na wykresie:dodaj tytuł, opisz oś X i Y, dodaj markery w punktach

# import matplotlib.pyplot as plt
#
# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# sprzedaz = [120, 150, 180, 160, 170, 210, 190]
# plt.plot(
#     dni,
#     sprzedaz,
#     color="black",
#     linewidth=2,
#     marker="s",)
# plt.title("Sprzedaz sklepu")
# plt.ylabel("Sprzedaz")
# plt.xlabel("Dni")
# plt.grid(True, linestyle="--", alpha=0.3) # siatka
# # dodanie wartosci liczbowych nad punkami
# for x, y in zip(dni, sprzedaz):
#     plt.text(x, y +3 , str(y), ha="center", fontsize=10, color="red")
#
# # Wyróżnienie jednego punktu — Sobota
# plt.annotate(
#     "Najwyższa sprzedaż",
#     xy=("Sob", 210),
#     xytext=("Pt", 215),
#     arrowprops=dict(arrowstyle="->", color="red", linewidth=2, shrinkB=5,shrinkA=2),
#     fontsize=10,
#     color="red")
# plt.show()
#


# --------------------------------------------------------------
# Zadanie 2 Matplotlib
#  Stwórz wykres słupkowy, który pokaże sprzedaż czterech produktów.
# Na wykresie:
#dodaj tytuł
# opisz osie
# import matplotlib.pyplot as plt
# produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
# sprzedaz = [25, 18, 40, 12]
#
# plt.bar(produkty,sprzedaz)
# plt.title("sprzedaz prduktow")
# plt.xlabel("produckty")
# plt.ylabel("sprzedaz")
# plt.grid(True, alpha=0.3)
# for x, y in zip(produkty, sprzedaz):
#     plt.text (x,y+1, str(y), color="red",ha="center",fontsize=10)
# plt.show()


# --------------------------------------------------------------
# # Zadanie 3 Matplotlib
# #  Oto wyniki testu studentów.
# # Stwórz histogram, który pokaże rozkład wyników.
# import matplotlib.pyplot as plt
# wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]
# plt.hist(wyniki, bins=5)
# plt.title("rozklad wynikow")
# plt.xlabel("wyniki")
# plt.ylabel("liczna wystapien")
# plt.show()
# #
