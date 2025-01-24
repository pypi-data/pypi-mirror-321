from typing import TypeVar, Type

from pydantic import BaseModel

from ..session import Session

BaseModelSubclass = TypeVar('BaseModelSubclass', bound=BaseModel)


class Estimator:
    """
    Base class for implementing estimators that process data through the API.

    This class provides the foundation for creating specific estimators by handling
    session management and input type validation. Subclasses should implement
    specific estimation logic while inheriting the base functionality.

    Attributes
    ----------
    estimator_name : str
        Name identifier for the estimator. Default is "EstimatorBase".
    estimator_version : str
        Version string for the estimator. Default is "1".
    prediction_version : str
        Version string for the prediction. Set to "1".
    estimator_id : None
        Identifier for a specific estimator instance, initialized as None.
    session : Session
        Session instance used for API communication.
    input_type : Type[BaseModelSubclass]
        Pydantic model class used for input validation.

    Notes
    -----
    The BaseModelSubclass type variable ensures that input_type must be
    a subclass of pydantic.BaseModel, enabling automatic input validation.
    """

    estimator_name = "EstimatorBase"
    estimator_version = "1"
    prediction_version = "1"

    def __init__(self, session: Session, input_type: Type[BaseModelSubclass]):
        """

        Parameters
        ----------
        session : Session
            Active session instance for API communication.
        input_type : Type[BaseModelSubclass]
            Pydantic model class that defines the expected input data structure.
        """
        self.estimator_id = None
        self.session = session
        self.input_type = input_type

    def get_route_prefix(self):
        return f"{self.estimator_name}/{self.estimator_version}"


class EstimatorCreationRequest(BaseModel):
    estimator_name: str
    session_id: str
    input_item_schema_b64: str
