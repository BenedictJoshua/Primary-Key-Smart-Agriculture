const { spawn } = require('child_process');

/**
 * Controller function to predict suitable crops by calling our native Python engine.
 * @param {Object} metrics - Agricultural input parameters from the frontend request body.
 */
function recommendCrop(metrics) {
    return new Promise((resolve, reject) => {
        // Extract features matching our Python CLI signature sequential order
        const { n, p, k, temperature, humidity, ph, rainfall } = metrics;
        
        // Define the path to your system's Python executable
        const pythonPath = 'C:\\Users\\Biju8\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe';
        const scriptPath = 'src/predict.py';
        
        // Spawn the Python process with arguments string-mapped sequentially
        const pythonProcess = spawn(pythonPath, [
            scriptPath, 
            String(n), 
            String(p), 
            String(k), 
            String(temperature), 
            String(humidity), 
            String(ph), 
            String(rainfall)
        ]);

        let outputData = '';
        let errorData = '';

        // Capture standard output from the Python runtime
        pythonProcess.stdout.on('data', (data) => {
            outputData += data.toString();
        });

        // Capture execution errors if any occur
        pythonProcess.stderr.on('data', (data) => {
            errorData += data.toString();
        });

        // Process exit cleanup handler
        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                return reject(new Error(`Python process exited with code ${code}. Error: ${errorData}`));
            }
            
            // Parse the output string "Prediction Result: crop_name"
            const match = outputData.match(/Prediction Result:\s*(\w+)/);
            if (match && match[1]) {
                resolve({ success: true, recommendedCrop: match[1] });
            } else {
                reject(new Error(`Failed to parse prediction output. Raw output: ${outputData}`));
            }
        });
    });
}

// ==========================================
// TEST SIMULATION
// Simulating an incoming HTTP Request Body from the Frontend UI
// ==========================================
const sampleRequestBody = {
    n: 90,
    p: 42,
    k: 43,
    temperature: 20.87,
    humidity: 82.00,
    ph: 6.50,
    rainfall: 202.93
};

console.log("Sending agricultural parameters to the Python Inference Engine...");
recommendCrop(sampleRequestBody)
    .then(result => console.log("Backend Response Object:", result))
    .catch(err => console.error("Integration Error encountered:", err.message));
