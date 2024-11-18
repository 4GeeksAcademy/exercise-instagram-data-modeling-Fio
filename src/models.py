import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# usuarios de Instagram con un nombre de usuario único, email y contraseña
class User (Base): 
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column (String(250), nullable= False)
    password = Column (String(100), nullable = False)

# Comentarios.
class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable= False)
   # create_date = Column(DataTime, default=datatime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)


 # Publicación de los users , hay descripción , imágen , la relación con el user  
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True) 
    description = Column(String(255))
    image_url = Column(String(255))
     # create_date = Column(DataTime, default=datatime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)




class Likes (Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True) 
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)








## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
