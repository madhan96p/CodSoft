package com.example.todolistapp.data // Adjust package name as needed

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey(autoGenerate = true)
    val id: Int = 0,
    var title: String,
    var description: String? = null,
    var isCompleted: Boolean = false,
    // You can add priority and dueDate fields here later
    // var priority: Int = 0, // e.g., 0 for low, 1 for medium, 2 for high
    // var dueDate: Long? = null // Store as timestamp
)