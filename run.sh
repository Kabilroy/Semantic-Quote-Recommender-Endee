#!/bin/bash

echo "🚀 Starting Quote Recommender..."
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Dependencies installed!"
echo ""
echo "🔗 Server starting at: http://localhost:8000"
echo ""

python main.py