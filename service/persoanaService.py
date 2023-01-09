from domain.persoana import Persoana
from repositories.inscriereRepository import InscriereRepository
from repositories.persoanaRepository import PersoanaRepository


class PersoanaService:
    def __init__(self, persoanaRepository: PersoanaRepository, inscriereRepository: InscriereRepository):
        self.__persoanaRepository = persoanaRepository
        self.__inscriereRepository = inscriereRepository

    def get_all(self):
        return self.__persoanaRepository.get_all_persoane()

    def adauga(self, idPersoana, nume, adresa, participari):
        persoana = Persoana(idPersoana, nume, adresa, participari)
        self.__persoanaRepository.adauga_persoana(persoana)

    def modifica(self, idPersoana, numeNew, adresaNew, participari):
        persoanaNew = Persoana(idPersoana, numeNew, adresaNew, participari)
        self.__persoanaRepository.modifica_persoana(persoanaNew)

    def sterge(self, idPersoana):
        inscrieri = self.__inscriereRepository.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana_i() == idPersoana:
                self.__inscriereRepository.sterge_inscriere(inscriere.get_idInscriere())
        self.__persoanaRepository.sterge_persoana(idPersoana)

    def cauta(self, idPersoana):
        aux= self.__persoanaRepository.cautare_persoana(idPersoana)
        if aux == None:
            raise Exception("Nu exista aceasta persoana!")
        else:
            return aux

    def top_participari(self):
        return self.__persoanaRepository.top_participari()