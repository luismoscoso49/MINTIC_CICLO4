package tutorial.mision.TIC.seguridad42.Modelos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document()
@NoArgsConstructor
@AllArgsConstructor
@Slf4j
public class Usuario {
    @Id
    private String _id;
    private String seudonimo;
    private String correo;
    private String contrasena;

    @DBRef
    private Rol rol;

    public Usuario(String seudonimo, String correo, String contrasena, Rol rol) {
        this.seudonimo = seudonimo;
        this.correo = correo;
        this.contrasena = contrasena;
        this.rol = rol;
    }

    /** */



    public String get_id() {
        return _id;
    }

    public String getSeudonimo() {
        return seudonimo;
    }

    public void setSeudonimo(String seudonimo) {
        this.seudonimo = seudonimo;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }

    @Override
    public String toString() {
        return "Rol{" +
                "_id='" + _id + '\'' +
                ", seudonimo='" + seudonimo + '\'' +
                ", correo='" + correo + '\'' +
                ", contrasena='" + contrasena + '\'' +
                '}';
    }
}
