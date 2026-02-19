from pydantic import BaseModel, EmailStr

# Base schema with email
class UserBase(BaseModel):
    email: EmailStr

# Schema used for creating a new user
class UserCreate(UserBase):
    password: str

# Schema used for responses (hides password)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

