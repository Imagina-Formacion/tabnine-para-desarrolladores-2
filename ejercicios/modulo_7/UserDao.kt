import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

/**
 * DAO de Room para la entidad User
 */
@Dao
interface UserDao {
    // Query para insertar un usuario
    /**
     * Inserta un usuario en la base de datos Room
     * @param user Usuario a insertar en la base de datos Room
     * @return ID del usuario insertado en la base de datos Room
     */
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertUser(user: User)

    // Query para obtener un usuario por ID
    @Query("SELECT * FROM user WHERE id = :userId")
    suspend fun getUserById(userId: Int): User
}