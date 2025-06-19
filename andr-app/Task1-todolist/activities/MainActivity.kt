package com.example.todolistapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.text2.input.delete
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.isEmpty
import androidx.compose.ui.semantics.error
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.wear.compose.foundation.weight
import com.example.todolistapp.data.Task
import com.example.todolistapp.ui.TaskViewModel
import com.example.todolistapp.ui.theme.ToDoListAppTheme // Create this theme or use a default

class MainActivity : ComponentActivity() {
    private val taskViewModel: TaskViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ToDoListAppTheme {
                androidx.compose.material3.Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = androidx.compose.material3.MaterialTheme.colorScheme.background
                ) {
                    TodoListApp(taskViewModel)
                }
            }
        }
    }
}

@androidx.annotation.OptIn(androidx.compose.material3.ExperimentalMaterial3Api::class)
@androidx.compose.runtime.Composable
fun TodoListApp(viewModel: TaskViewModel) {
    val tasks by viewModel.allTasks.collectAsState()
    val showDialog by viewModel.showDialog.observeAsState(false)
    val currentTask by viewModel.currentTask.observeAsState()

    androidx.compose.material3.Scaffold(
        topBar = {
            androidx.compose.material3.TopAppBar(
                title = { androidx.compose.material3.Text("To-Do List") },
                colors = androidx.compose.material3.TopAppBarDefaults.topAppBarColors(
                    containerColor = androidx.compose.material3.MaterialTheme.colorScheme.primaryContainer,
                    titleContentColor = androidx.compose.material3.MaterialTheme.colorScheme.primary
                )
            )
        },
        floatingActionButton = {
            androidx.compose.material3.FloatingActionButton(onClick = { viewModel.openDialog() }) {
                androidx.compose.material3.Icon(Icons.Filled.Add, "Add Task")
            }
        }
    ) { paddingValues ->
        androidx.compose.foundation.layout.Column(modifier = Modifier.padding(paddingValues)) {
            if (tasks.isEmpty()) {
                androidx.compose.foundation.layout.Box(
                    modifier = Modifier.fillMaxSize(),
                    contentAlignment = Alignment.Center
                ) {
                    androidx.compose.material3.Text("No tasks yet. Add one!", fontSize = 18.sp)
                }
            } else {
                LazyColumn(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(8.dp)
                ) {
                    items(tasks, key = { task -> task.id }) { task ->
                        TaskItem(
                            task = task,
                            onCheckedChange = { isChecked ->
                                viewModel.onTaskCheckedChanged(task, isChecked)
                            },
                            onEditClick = { viewModel.openDialog(task) },
                            onDeleteClick = { viewModel.delete(task) }
                        )
                        androidx.compose.material3.Divider()
                    }
                }
            }
        }

        if (showDialog) {
            TaskEditDialog(
                task = currentTask, // Can be null for new task, or existing for edit
                onDismiss = { viewModel.closeDialog() },
                onSave = { title, description ->
                    viewModel.saveTask(title, description)
                }
            )
        }
    }
}

@androidx.compose.runtime.Composable
fun TaskItem(
    task: Task,
    onCheckedChange: (Boolean) -> Unit,
    onEditClick: () -> Unit,
    onDeleteClick: () -> Unit
) {
    androidx.compose.foundation.layout.Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        androidx.compose.material3.Checkbox(
            checked = task.isCompleted,
            onCheckedChange = onCheckedChange
        )
        androidx.compose.foundation.layout.Spacer(modifier = Modifier.width(8.dp))
        androidx.compose.foundation.layout.Column(modifier = Modifier.weight(1f)) {
            androidx.compose.material3.Text(
                text = task.title,
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold,
                textDecoration = if (task.isCompleted) TextDecoration.LineThrough else null
            )
            task.description?.let {
                if (it.isNotBlank()) {
                    androidx.compose.material3.Text(
                        text = it,
                        fontSize = 14.sp,
                        textDecoration = if (task.isCompleted) TextDecoration.LineThrough else null
                    )
                }
            }
        }
        androidx.compose.material3.IconButton(onClick = onEditClick) {
            androidx.compose.material3.Icon(Icons.Filled.Edit, contentDescription = "Edit Task")
        }
        androidx.compose.material3.IconButton(onClick = onDeleteClick) {
            androidx.compose.material3.Icon(Icons.Filled.Delete, contentDescription = "Delete Task")
        }
    }
}

@androidx.annotation.OptIn(androidx.compose.material3.ExperimentalMaterial3Api::class)
@androidx.compose.runtime.Composable
fun TaskEditDialog(
    task: Task?, // Null for new task, existing task for editing
    onDismiss: () -> Unit,
    onSave: (title: String, description: String?) -> Unit
) {
    var title by androidx.compose.runtime.remember { androidx.compose.runtime.mutableStateOf(task?.title ?: "") }
    var description by androidx.compose.runtime.remember { androidx.compose.runtime.mutableStateOf(task?.description ?: "") }
    var titleError by androidx.compose.runtime.remember { androidx.compose.runtime.mutableStateOf<String?>(null) }

    androidx.compose.material3.AlertDialog(
        onDismissRequest = onDismiss,
        title = { androidx.compose.material3.Text(if (task?.id == 0 || task == null) "Add New Task" else "Edit Task") },
        text = {
            androidx.compose.foundation.layout.Column {
                androidx.compose.material3.OutlinedTextField(
                    value = title,
                    onValueChange = {
                        title = it
                        titleError = if (it.isBlank()) "Title cannot be empty" else null
                    },
                    label = { androidx.compose.material3.Text("Title*") },
                    isError = titleError != null,
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth()
                )
                if (titleError != null) {
                    androidx.compose.material3.Text(text = titleError!!, color = androidx.compose.material3.MaterialTheme.colorScheme.error, style = androidx.compose.material3.MaterialTheme.typography.bodySmall)
                }
                androidx.compose.foundation.layout.Spacer(modifier = Modifier.height(8.dp))
                androidx.compose.material3.OutlinedTextField(
                    value = description,
                    onValueChange = { description = it },
                    label = { androidx.compose.material3.Text("Description (Optional)") },
                    modifier = Modifier.fillMaxWidth(),
                    minLines = 3
                )
            }
        },
        confirmButton = {
            androidx.compose.material3.Button(
                onClick = {
                    if (title.isNotBlank()) {
                        onSave(title, description.ifBlank { null }) // Save null if description is empty
                    } else {
                        titleError = "Title cannot be empty"
                    }
                }
            ) {
                androidx.compose.material3.Text("Save")
            }
        },
        dismissButton = {
            androidx.compose.material3.TextButton(onClick = onDismiss) {
                androidx.compose.material3.Text("Cancel")
            }
        }
    )
}


@Preview(showBackground = true)
@androidx.compose.runtime.Composable
fun DefaultPreview() {
    ToDoListAppTheme {
        // You can pass a mock ViewModel or just preview specific Composables
        // For simplicity, we'll show a preview of the TaskItem
        TaskItem(
            task = Task(id = 1, title = "Sample Task", description = "This is a description", isCompleted = false),
            onCheckedChange = {},
            onEditClick = {},
            onDeleteClick = {}
        )
    }
}

// Create a Theme.kt file in your ui/theme package or use a default one.
// Example: ui/theme/Theme.kt
// package com.example.todolistapp.ui.theme
//
// import androidx.compose.material3.MaterialTheme
// import androidx.compose.material3.lightColorScheme // or darkColorScheme
// import androidx.compose.runtime.Composable
//
// private val LightColorScheme = lightColorScheme(
//    primary = /* your primary color */,
//    secondary = /* your secondary color */,
//    tertiary = /* your tertiary color */
//    /* ...other colors */
// )
//
// @Composable
// fun ToDoListAppTheme(
//    content: @Composable () -> Unit
// ) {
//    MaterialTheme(
//        colorScheme = LightColorScheme,
//        typography = Typography, // Define your Typography
//        content = content
//    )
// }
//
// // Also define ui/theme/Typography.kt
// package com.example.todolistapp.ui.theme
//
// import androidx.compose.material3.Typography
// import androidx.compose.ui.text.TextStyle
// import androidx.compose.ui.text.font.FontFamily
// import androidx.compose.ui.text.font.FontWeight
// import androidx.compose.ui.unit.sp
//
// val Typography = Typography(
//    bodyLarge = TextStyle(
//        fontFamily = FontFamily.Default,
//        fontWeight = FontWeight.Normal,
//        fontSize = 16.sp
//    )
//    /* Other text styles to override */
// )