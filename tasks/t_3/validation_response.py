from pydantic import BaseModel, Field


class OutputValidationResponse(BaseModel):
    is_valid: bool = Field(
        description="True if NO forbidden PII or sensitive personal/financial data is leaked in the output. False if ANY forbidden PII is disclosed."
    )
    leaked_entities: list[str] = Field(
        default_factory=list,
        description="List of detected leaked sensitive fields (e.g. ssn, credit_card, address, date_of_birth, bank_account, income, driver_license)."
    )
    reason: str = Field(
        description="Detailed explanation of the validation judgment."
    )
