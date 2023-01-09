from domain.eveniment import Eveniment
from repositories.evenimentRepository import EvenimentRepository
from repositories.inscriereRepository import InscriereRepository


class EvenimentService:
    def __init__(self, evenimentRepository: EvenimentRepository, inscriereRepository: InscriereRepository):
        self.__evenimentRepository = evenimentRepository
        self.__inscriereRepository = inscriereRepository

    def get_all(self):
        return self.__evenimentRepository.get_all_evenimente()

    def adauga(self, idEveniment, data, timp, descriere, participanti):
        eveniment = Eveniment(idEveniment, data, timp, descriere, participanti)
        self.__evenimentRepository.adauga_eveniment(eveniment)

    def modifica(self, idEveniment, dataNew, timpNew, descriereNew, participanti):
        evenimentNew = Eveniment(idEveniment, dataNew, timpNew, descriereNew, participanti)
        self.__evenimentRepository.modifica_eveniment(evenimentNew)

    def sterge(self, idEveniment):
        inscrieri = self.__inscriereRepository.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idEveniment_i() == idEveniment:
                self.__inscriereRepository.sterge_inscriere(inscriere.get_idInscriere())
        self.__evenimentRepository.sterge_eveniment(idEveniment)

    def cauta(self, idEveniment):
        aux = self.__evenimentRepository.cautare_eveniment(idEveniment)
        if aux == None:
            raise Exception("Nu exista acest eveniment!")
        else:
            return aux

    def ordonare_dupa_descriere(self):
        return self.__evenimentRepository.sortare_dupa_descriere()

    def ordonare_dupa_data(self):
        return self.__evenimentRepository.sortare_dupa_data()

    def top20_dupa_participanti(self):
        return self.__evenimentRepository.top20_participari()

