package Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import Modelos.Rol;

public interface RepositorioRol  extends MongoRepository<Rol,String> {
}
