from pydantic import BaseModel , ConfigDict , Field

class PostBase(BaseModel):
     author : str = Field(min_length= 3 , max_length= 50)
     title : str = Field(min_length= 3)
     content : str = Field(min_length= 3)


class PostCreate(PostBase):
     pass

class PostResponse(PostBase):
     model_config = ConfigDict(from_attributes=True)
     id : int
     date_posted : str