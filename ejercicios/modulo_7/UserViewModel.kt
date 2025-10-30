import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.runtime.LiveData
import androidx.compose.runtime.MutableLiveData
import android.app.Appication

// ViewModel para gestionar los datos de un usuario
class UserViewModel(application: Application) : AndroidViewModel(application) {
    private val _user = MutableLiveData<User>()
    val user: LiveData<User> = _user

    // Función para obtener los datos del usuario por ID
    fun fetchUser(userId: Int) {
        // Llama a la API para obtener los datos del usuario
        // y actualiza el LiveData con los datos obtenidos
        _user.value = User(userId, "John Doe", "johndoe@example.com")
    }
}