class EvenimentRepository:
    def __init__(self):
        self.__evenimente = {}

    def get_all_evenimente(self):
        return list(self.__evenimente.values())

    def get_by_idEveniment(self, idEveniment):
        evenimente = self.get_all_evenimente()
        for eveniment in evenimente:
            if eveniment.get_idEveniment() == idEveniment:
                return eveniment
        return None

    def adauga_eveniment(self, eveniment):
        if self.get_by_idEveniment(eveniment.get_idEveniment()) is not None:
            raise KeyError("Exista deja un eveniment cu id-ul dat!")
        self.__evenimente[eveniment.get_idEveniment()] = eveniment

    def modifica_eveniment(self, evenimentNew):
        if self.get_by_idEveniment(evenimentNew.get_idEveniment()) is None:
            raise KeyError("Nu exista eveniment cu id-ul dat!")
        self.__evenimente[evenimentNew.get_idEveniment()] = evenimentNew

    def sterge_eveniment(self, idEveniment):
        if self.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista eveniment cu id-ul dat!")
        self.__evenimente.pop(idEveniment)

    def nr_evenimente(self):
        return int(len(self.__evenimente))

    def sortare_dupa_descriere(self):
        return sorted(self.__evenimente.values(), key=lambda x: x.get_descriere())

    def sortare_dupa_data(self):
        return sorted(self.__evenimente.values(), key=lambda x: x.get_data())

    def sortare_dupa_participanti(self):
        return sorted(self.__evenimente.values(), key=lambda x: x.get_participanti(), reverse = True)

    def participanti_plus(self, idEveniment):
        if self.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu acest id!")
        entitate = self.get_by_idEveniment(idEveniment)
        part = int(entitate.get_participanti())
        self.get_by_idEveniment(idEveniment).set_participanti(part + 1)

    def participanti_minus(self, idEveniment):
        if self.get_by_idEveniment(idEveniment) is None:
            raise ValueError("Nu exista un eveniment cu acest id!")
        entitate = self.get_by_idEveniment(idEveniment)
        part = int(entitate.get_participanti())
        self.get_by_idEveniment(idEveniment).set_participanti(part - 1)

    def top20_participari(self):
        lst1 = []
        percent = 0.2
        n = self.nr_evenimente()
        nr = int(percent * n)
        lst2 = self.sortare_dupa_participanti()
        for i in range (nr):
            lst1.append(lst2[i])
        return lst1

    def cautare_eveniment(self, idEveniment):
        evenimente = self.get_all_evenimente()
        for eveniment in evenimente:
            if eveniment.get_idEveniment() == idEveniment:
                return eveniment
        return None