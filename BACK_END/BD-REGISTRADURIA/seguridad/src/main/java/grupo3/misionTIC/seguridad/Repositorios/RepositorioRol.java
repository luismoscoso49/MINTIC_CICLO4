package grupo3.misionTIC.seguridad.Repositorios;

import grupo3.misionTIC.seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String> {
}
