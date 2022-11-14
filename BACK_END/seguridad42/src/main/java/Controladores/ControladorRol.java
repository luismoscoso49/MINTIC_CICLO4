package Controladores;

import Modelos.Rol;
import Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class ControladorRol {

    @Autowired
    private RepositorioRol repositorioRol;

    @GetMapping("")
    public List<Rol> index() {
        return this.repositorioRol.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Rol create(@RequestBody Rol infoRol) {
        return this.repositorioRol.save(infoRol);
    }

    @GetMapping("{id}")
    /** {id} es una variable
     * pathvariable dice que el parametro es el de la ruta
     * */
    public Rol show(@PathVariable String id) {
        Rol rolActual = this.repositorioRol.findById(id).orElse(null);
        return rolActual;
    }

    @PutMapping("{id}")
    public Rol update(@PathVariable String id, @RequestBody Rol
            infoRol) {
        Rol rolActual = this.repositorioRol
                .findById(id)
                .orElse(null);
        if (rolActual != null) {
            rolActual.setNombre(infoRol.getNombre());
            return this.repositorioRol.save(rolActual);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Rol rolActual = this.repositorioRol
                .findById(id)
                .orElse(null);
        if (rolActual != null) {
            this.repositorioRol.delete(rolActual);
        }
    }



}
