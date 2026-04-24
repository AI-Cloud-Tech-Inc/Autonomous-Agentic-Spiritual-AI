'use client';

import { useState } from 'react';
import Link from 'next/link';

export default function CreateFilm() {
  const [formData, setFormData] = useState({
    prompt: '',
    style: 'cinematic',
    duration: 30,
    model: 'claude-opus-4-6',
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await fetch('http://localhost:8000/api/v1/autonomous/create-film', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to create film');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <header className="bg-gray-800 border-b border-gray-700 p-6">
        <div className="container mx-auto">
          <Link href="/" className="text-indigo-400 hover:text-indigo-300 mb-2 inline-block">
            ← Back to Dashboard
          </Link>
          <h1 className="text-3xl font-bold">🎬 Create Your Film</h1>
          <p className="text-gray-400 mt-2">Transform your vision into reality with autonomous AI agents</p>
        </div>
      </header>

      <main className="container mx-auto p-6 max-w-3xl">
        <form onSubmit={handleSubmit} className="bg-gray-800 p-8 rounded-lg border border-gray-700">
          <div className="mb-6">
            <label className="block text-sm font-medium mb-2">
              Film Concept <span className="text-red-400">*</span>
            </label>
            <textarea
              value={formData.prompt}
              onChange={(e) => setFormData({ ...formData, prompt: e.target.value })}
              placeholder="Describe your film idea... (e.g., 'A cyberpunk city at night with neon lights and flying vehicles')"
              rows={4}
              required
              disabled={loading}
              className="w-full p-3 bg-gray-700 border border-gray-600 rounded focus:border-indigo-500 focus:outline-none"
            />
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div>
              <label className="block text-sm font-medium mb-2">Visual Style</label>
              <select
                value={formData.style}
                onChange={(e) => setFormData({ ...formData, style: e.target.value })}
                disabled={loading}
                className="w-full p-3 bg-gray-700 border border-gray-600 rounded focus:border-indigo-500 focus:outline-none"
              >
                <option value="cinematic">Cinematic</option>
                <option value="documentary">Documentary</option>
                <option value="anime">Anime</option>
                <option value="cartoon">Cartoon</option>
                <option value="realistic">Realistic</option>
                <option value="sci-fi">Sci-Fi</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">Duration (seconds)</label>
              <input
                type="number"
                value={formData.duration}
                onChange={(e) => setFormData({ ...formData, duration: parseInt(e.target.value) })}
                min="10"
                max="300"
                step="10"
                disabled={loading}
                className="w-full p-3 bg-gray-700 border border-gray-600 rounded focus:border-indigo-500 focus:outline-none"
              />
            </div>
          </div>

          <div className="mb-6">
            <label className="block text-sm font-medium mb-2">AI Model</label>
            <select
              value={formData.model}
              onChange={(e) => setFormData({ ...formData, model: e.target.value })}
              disabled={loading}
              className="w-full p-3 bg-gray-700 border border-gray-600 rounded focus:border-indigo-500 focus:outline-none"
            >
              <option value="claude-opus-4-6">Claude Opus 4.6 (Anthropic) — Most Powerful</option>
              <option value="claude-sonnet-4-6">Claude Sonnet 4.6 (Anthropic) — Balanced</option>
              <option value="claude-haiku-4-5">Claude Haiku 4.5 (Anthropic) — Fastest</option>
              <option value="gpt-4">GPT-4 (OpenAI)</option>
            </select>
          </div>

          <button
            type="submit"
            disabled={loading || !formData.prompt}
            className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-gray-600 text-white font-bold py-4 rounded-lg text-lg transition"
          >
            {loading ? '🎬 Creating Film...' : '🚀 Create Film'}
          </button>
        </form>

        {loading && (
          <div className="mt-8 bg-gray-800 p-6 rounded-lg border border-gray-700">
            <h3 className="text-xl font-bold mb-4 text-indigo-400">Production Progress</h3>
            <div className="space-y-3">
              <div className="flex items-center gap-3">
                <div className="animate-spin h-5 w-5 border-2 border-indigo-400 border-t-transparent rounded-full"></div>
                <span>Director creating vision...</span>
              </div>
            </div>
          </div>
        )}

        {result && (
          <div className="mt-8 bg-gray-800 p-6 rounded-lg border border-green-500">
            <h3 className="text-xl font-bold mb-4 text-green-400">✅ Film Created Successfully!</h3>
            <div className="space-y-3">
              <p><strong>Film ID:</strong> {result.film_id}</p>
              <p><strong>Status:</strong> {result.status}</p>
              {result.scenes && <p><strong>Scenes:</strong> {result.scenes.length}</p>}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
