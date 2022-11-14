package Controladores;

import Modelos.Permiso;
import Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;
//import tutorial.mision.TIC.seguridad42.Repositorios.RepositorioPermiso;


@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso repositorioPermiso;

    @GetMapping("")
    public List<Permiso> index() {
        return this.repositorioPermiso.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Permiso create(@RequestBody Permiso infoPermiso) {
        return this.repositorioPermiso.save(infoPermiso);
    }

    @GetMapping("{id}")
    /** {id} es una variable
     * pathvariable dice que el parametro es el de la ruta
     * */
    public Permiso show(@PathVariable String id) {
        Permiso permisoActual = this.repositorioPermiso.findById(id).orElse(null);
        return permisoActual;
    }

    @PutMapping("{id}")
    public Permiso update(@PathVariable String id, @RequestBody Permiso
            infoPermiso) {
        Permiso permisoActual = this.repositorioPermiso
                .findById(id)
                .orElse(null);
        if (permisoActual != null) {
            permisoActual.setUrl(infoPermiso.getUrl());
            permisoActual.setMetodo(infoPermiso.getMetodo());
            return this.repositorioPermiso.save(permisoActual);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Permiso permisoActual = this.repositorioPermiso
                .findById(id)
                .orElse(null);
        if (permisoActual != null) {
            this.repositorioPermiso.delete(permisoActual);
        }
    }
}

