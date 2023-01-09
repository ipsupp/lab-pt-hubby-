from domain.exceptions.duplicateError import DuplicateError
from domain.inscriere import Inscriere
from repositories.evenimentRepository import EvenimentRepository
from repositories.inscriereRepository import InscriereRepository
from repositories.persoanaRepository import PersoanaRepository


class InscriereService:
    def __init__(self, inscriereRepository: InscriereRepository, persoanaRepository: PersoanaRepository, evenimentRepository: EvenimentRepository):
        self.__inscriereRepository = inscriereRepository
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def get_all(self):
        return self.__inscriereRepository.get_all_inscrieri()

    def adauga(self, idInscriere, idPersoana, idEveniment):
        if self.__persoanaRepository.get_by_idPersoana(idPersoana) is None:
            raise KeyError("Nu exista o persoana cu id-ul dat!")
        if self.__evenimentRepository.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu id-ul dat!")
        inscrieri = self.__inscriereRepository.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana_i() == idPersoana and inscriere.get_idEveniment_i() == idEveniment:
                raise DuplicateError("Persoana este deja isncrisa la acest eveniment!")
        inscriere = Inscriere(idInscriere, idPersoana, idEveniment)
        self.__inscriereRepository.adauga_inscriere(inscriere)

    def sterge(self, idPersoana, idEveniment):
        self.__inscriereRepository.sterge_inscriere(idPersoana, idEveniment)

