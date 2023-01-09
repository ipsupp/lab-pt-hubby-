class PersoanaRepository:
    def __init__(self):
        self.__persoane = {}

    def get_all_persoane(self):
        return list(self.__persoane.values())

    def get_by_idPersoana(self, idPersoana):
        persoane = self.get_all_persoane()
        for persoana in persoane:
            if persoana.get_idPersoana() == idPersoana:
                return persoana
        return None

    def adauga_persoana(self, persoana):
        if self.get_by_idPersoana(persoana.get_idPersoana()) is not None:
            raise KeyError("Exista deja persoana cu id-ul dat!")
        self.__persoane[persoana.get_idPersoana()] = persoana

    def modifica_persoana(self, persoanaNew):
        if self.get_by_idPersoana(persoanaNew.get_idPersoana()) is None:
            raise KeyError("Nu exista persoana cu id-ul dat!")
        self.__persoane[persoanaNew.get_idPersoana()] = persoanaNew

    def sterge_persoana(self, idPersoana):
        if self.get_by_idPersoana(idPersoana) is None:
            raise KeyError("Nu exista persoana cu id-ul dat!")
        self.__persoane.pop(idPersoana)

    def nr_persoane(self):
        return int(len(self.__persoane))

    def participari_plus(self, idPersoana):
        if self.get_by_idPersoana(idPersoana) is None:
            raise ValueError ("Nu exista persoana cu acest id!")
        entitate =  self.get_by_idPersoana(idPersoana)
        part = int(entitate.get_participari())
        self.get_by_idPersoana(idPersoana).set_participari(part + 1)
###
    def participari_minus(self, idPersoana):
        if self.get_by_idPersoana(idPersoana) is None:
            raise ValueError ("Nu exista persoana cu acest id!")
        entitate = self.get_by_idPersoana(idPersoana)
        part = int(entitate.get_participari())
        self.get_by_idPersoana(idPersoana).set_participari(part - 1)

    def sortare_dupa_participari(self):
        return sorted(self.__persoane.values(), key = lambda x: x.get_participari, reverse = True)

    def top_participari(self):
        maxx = 0
        persoane = self.get_all_persoane()
        lst = []
        for persoana in persoane:
            if persoana.get_participari() > maxx:
                maxx = int(persoana.get_participari())

        for persoana in persoane:
            if persoana.get_participari() == maxx:
                lst.append(persoana)
        return lst

    def cautare_persoana(self, idPersoana):
        persoane = self.get_all_persoane()
        for persoana in persoane:
            if persoana.get_idPersoana() == idPersoana:
                return persoana
        return None
