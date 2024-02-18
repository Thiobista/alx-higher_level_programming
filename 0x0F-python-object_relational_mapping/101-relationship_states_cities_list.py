#!/usr/bin/python3

""" lists all State objects, and corresponding City objects,
contained in the database """

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    inp = sys.argv
    if len(inp) < 4:

