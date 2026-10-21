import React, { useState } from 'react';
import { X, Sparkles, Check, AlertCircle, ArrowRight } from 'lucide-react';
import axios from 'axios';

export function TitleScorerModal({ isOpen, onClose, initialTitle = '' }) {
  if (!isOpen) return null;

  const [title, setTitle] = useState(initialTitle || 'How to build full stack web apps in Python');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleScore = async () => {
    if (!title.trim() || loading) return;
    setLoading(true);
    try {
      const res = await axios.post('/api/ml/score-title', { title });
      setResult(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-[#0f172a] border border-slate-800 rounded-3xl w-full max-w-xl p-6 shadow-2xl relative">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 p-2 rounded-lg bg-slate-800 text-slate-400 hover:text-white transition"
        >
          <X className="w-4 h-4" />
        </button>

        <div className="flex items-center gap-2 mb-2">
          <Sparkles className="w-5 h-5 text-indigo-400" />
          <h3 className="text-lg font-bold text-white">Title & Thumbnail Click-Potential Scorer</h3>
        </div>
        <p className="text-xs text-slate-400 mb-5">
          Predict click potential, CTR hooks, and emotional resonance before publishing.
        </p>

        {/* Input area */}
        <div className="space-y-3">
          <div className="flex gap-2">
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter prospective video title..."
              className="flex-1 bg-slate-800/80 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
            <button
              onClick={handleScore}
              disabled={loading}
              className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 font-semibold text-sm text-white transition disabled:opacity-50"
            >
              {loading ? 'Analyzing...' : 'Analyze'}
            </button>
          </div>
        </div>

        {/* Results */}
        {result && (
          <div className="mt-6 pt-5 border-t border-slate-800 space-y-4">
            <div className="flex items-center justify-between bg-slate-900/60 p-4 rounded-2xl border border-slate-800">
              <div>
                <span className="text-xs text-slate-400 uppercase font-semibold">Predicted CTR Potential</span>
                <div className="flex items-baseline gap-2 mt-0.5">
                  <span className="text-3xl font-black text-white">{result.score}</span>
                  <span className="text-sm text-slate-400">/ 100</span>
                </div>
              </div>
              <div className="w-12 h-12 rounded-xl bg-gradient-to-tr from-indigo-500 to-emerald-400 flex items-center justify-center text-xl font-black text-white shadow-lg">
                {result.grade}
              </div>
            </div>

            {/* Strengths & Improvements */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-xl p-3">
                <span className="text-xs font-bold text-emerald-400 flex items-center gap-1.5 mb-1.5">
                  <Check className="w-3.5 h-3.5" /> Strengths
                </span>
                <ul className="text-xs text-slate-300 space-y-1">
                  {result.strengths.map((s, i) => (
                    <li key={i}>• {s}</li>
                  ))}
                </ul>
              </div>

              <div className="bg-amber-500/10 border border-amber-500/20 rounded-xl p-3">
                <span className="text-xs font-bold text-amber-400 flex items-center gap-1.5 mb-1.5">
                  <AlertCircle className="w-3.5 h-3.5" /> Growth Optimizations
                </span>
                <ul className="text-xs text-slate-300 space-y-1">
                  {result.improvements.map((imp, i) => (
                    <li key={i}>• {imp}</li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Suggested Variations */}
            {result.suggested_variations && (
              <div className="bg-slate-800/40 border border-slate-700/60 rounded-xl p-3.5">
                <span className="text-xs font-bold text-indigo-300 block mb-2">
                  High-Impact Suggested Variations:
                </span>
                <div className="space-y-1.5">
                  {result.suggested_variations.map((v, i) => (
                    <button
                      key={i}
                      onClick={() => setTitle(v)}
                      className="w-full text-left p-2 rounded-lg bg-slate-900/60 hover:bg-slate-800 text-xs text-slate-200 border border-slate-800 flex items-center justify-between group transition"
                    >
                      <span>"{v}"</span>
                      <ArrowRight className="w-3 h-3 text-slate-500 group-hover:text-indigo-400 transition" />
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
