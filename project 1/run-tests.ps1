./k6.exe run script-test-index.js --env PORT="5000";
./k6.exe run script-test-post.js --env PORT="5000";
./k6.exe run script-test-redirect.js --env PORT="5000";
./k6.exe run script-test-random.js --env PORT="5000";
./k6.exe run script-test-index.js --env PORT="3000";
./k6.exe run script-test-post.js --env PORT="3000";
./k6.exe run script-test-redirect.js --env PORT="3000";
./k6.exe run script-test-random.js --env PORT="3000";
./k6.exe run script-test-index.js --env PORT="8000";
./k6.exe run script-test-post.js --env PORT="8000";
./k6.exe run script-test-redirect.js --env PORT="8000";
./k6.exe run script-test-random.js --env PORT="8000";