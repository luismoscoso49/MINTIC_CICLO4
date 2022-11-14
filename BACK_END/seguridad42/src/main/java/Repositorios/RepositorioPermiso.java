package Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import Modelos.Permiso;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
}
