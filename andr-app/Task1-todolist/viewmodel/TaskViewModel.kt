package com.example.todolistapp.ui // Adjust package name

import android.app.Application
import androidx.compose.animation.core.copy
import androidx.compose.foundation.text2.input.delete
import androidx.compose.foundation.text2.input.insert
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.viewModelScope
import com.example.todolistapp.data.AppDatabase
import com.example.todolistapp.data.Task
import com.example.todolistapp.data.TaskRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class TaskViewModel(application: Application) : AndroidViewModel(application) {

    private val repository: TaskRepository
    val allTasks: StateFlow<List<Task>> // Use StateFlow for Compose

    // For managing the dialog state and current task being edited/created
    private val _showDialog = MutableLiveData(false)
    val showDialog: LiveData<Boolean> = _showDialog

    private val _currentTask = MutableLiveData<Task?>(null)
    val currentTask: LiveData<Task?> = _currentTask

    init {
        val taskDao = AppDatabase.getDatabase(application).taskDao()
        repository = TaskRepository(taskDao)
        allTasks = repository.allTasks.stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000), // Keep active for 5s after last subscriber
            initialValue = emptyList()
        )
    }

    fun insert(task: Task) = viewModelScope.launch {
        repository.insert(task)
    }

    fun update(task: Task) = viewModelScope.launch {
        repository.update(task)
    }

    fun delete(task: Task) = viewModelScope.launch {
        repository.delete(task)
    }

    fun onTaskCheckedChanged(task: Task, isChecked: Boolean) {
        val updatedTask = task.copy(isCompleted = isChecked)
        update(updatedTask)
    }

    // --- Dialog Management ---
    fun openDialog(task: Task? = null) {
        _currentTask.value = task ?: Task(title = "", description = "") // New task if null
        _showDialog.value = true
    }

    fun closeDialog() {
        _showDialog.value = false
        _currentTask.value = null // Reset current task
    }

    fun saveTask(title: String, description: String?) {
        viewModelScope.launch {
            val taskToSave = _currentTask.value?.copy(
                title = title,
                description = description
            ) ?: Task(title = title, description = description) // Should not happen if dialog is managed correctly

            if (taskToSave.id == 0) { // New task
                repository.insert(taskToSave)
            } else { // Existing task
                repository.update(taskToSave)
            }
            closeDialog()
        }
    }
}