package grupo3.misionTIC.seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import grupo3.misionTIC.seguridad.Modelos.PermisosRoles;
public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}

