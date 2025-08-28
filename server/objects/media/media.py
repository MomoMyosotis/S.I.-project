# first line

# ============================================================
# MEDIA BASE CLASS
# ============================================================
# Qui definiamo la classe base "Media" che rappresenta un generico contenuto
# multimediale (es. canzone, documento, video). Non è pensata per essere
# usata direttamente ma come "contratto" da cui ereditano le sottoclassi.
# ============================================================

# ABC = Abstract Base Class → libreria di Python per creare classi astratte
# (cioè classi che non possono essere istanziate direttamente).
# Le classi figlie DEVONO implementare i metodi definiti come @abstractmethod.
from abc import ABC, abstractmethod

# Per i tipi (Optional = può essere None, Dict/Any = per serializzazione JSON)
from typing import Optional, Dict, Any

class Media(ABC):
    """
    Classe astratta base per rappresentare un oggetto 'Media'.
    Tutti i tipi di media (Song, Document, Video, ecc.) erediteranno da qui.
    """

    def __init__(self,
                id: Optional[int] = None,
                title: Optional[str] = None,
                year: Optional[int] = None,
                description: Optional[str] = None,
                link: Optional[str] = None):
        """
        Inizializza un oggetto Media con campi comuni.
        - id: identificativo unico (DB)
        - title: titolo del contenuto
        - year: anno di pubblicazione
        - description: descrizione/testo libero
        - link: collegamento a file esterni o risorsa web
        """
        self.id = id
        self.title = title
        self.year = year
        self.description = description
        self.link = link

    # Ogni sottoclasse (Song, Document, ecc.) deve specificare
    # quale tipo di media rappresenta
    @abstractmethod
    def media_type(self) -> str:
        pass

        # Serializza l’oggetto in un dizionario (utile per API/JSON).
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "description": self.description,
            "link": self.link,
            "media_type": self.media_type()
        }

        # Rappresentazione leggibile in console
    def __repr__(self) -> str:
        return f"<{self.media_type().capitalize()} id={self.id}, title={self.title}>"

# last line