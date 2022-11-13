package grupo3.misionTIC.seguridad.Repositorios;

import grupo3.misionTIC.seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
}
