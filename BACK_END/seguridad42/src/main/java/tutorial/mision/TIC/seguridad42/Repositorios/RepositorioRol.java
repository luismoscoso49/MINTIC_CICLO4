package tutorial.mision.TIC.seguridad42.Repositorios;

import tutorial.mision.TIC.seguridad42.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Usuario,String> {
}
