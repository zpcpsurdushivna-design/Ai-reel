package com.aireelagent;

import android.content.Intent;
import android.net.Uri;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private final String BACKEND_URL = "https://your-backend-domain.com";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnYouTube = findViewById(R.id.btnConnectYouTube);
        Button btnInstagram = findViewById(R.id.btnConnectInstagram);
        Button btnStart = findViewById(R.id.btnStartAutomation);

        btnYouTube.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(BACKEND_URL + "/oauth/youtube/start"));
            startActivity(intent);
        });

        btnInstagram.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(BACKEND_URL + "/oauth/instagram/start"));
            startActivity(intent);
        });

        btnStart.setOnClickListener(v -> {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(BACKEND_URL + "/start-auto"));
            startActivity(intent);
        });
    }
}
