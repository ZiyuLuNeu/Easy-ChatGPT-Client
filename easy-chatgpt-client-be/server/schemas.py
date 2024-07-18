from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    settings: dict

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True