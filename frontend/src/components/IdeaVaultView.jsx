import React, { useState } from 'react';
import { Lightbulb, Plus, Star, Sparkles, Clock, CheckCircle } from 'lucide-react';

export function IdeaVaultView({ ideas, onAddIdea, onScoreTitle }) {
  const [newTitle, setNewTitle] = useState('');
  const [effort, setEffort] = useState('Medium (3-5h)');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newTitle.trim()) return;
    onAddIdea(newTitle, 'user', effort);
    setNewTitle('');
  };

  return (
    <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 mb-8">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-5">
        <div>
          <div className="flex items-center gap-2">
            <Lightbulb className="w-5 h-5 text-amber-400" />
            <h3 className="text-base font-bold text-white">Idea Vault & AI Ranking</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Prioritize content concepts scored by predicted engagement, search velocity, and production effort.
          </p>
        </div>

        {/* Quick add form */}
        <form onSubmit={handleSubmit} className="flex items-center gap-2">
          <input
            type="text"
            value={newTitle}
            onChange={(e) => setNewTitle(e.target.value)}
            placeholder="Add new video idea..."
            className="bg-slate-800/80 border border-slate-700 rounded-xl px-3.5 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 w-60"
          />
          <button
            type="submit"
            className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-semibold text-white transition"
          >
            <Plus className="w-3.5 h-3.5" /> Add
          </button>
        </form>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {ideas && ideas.length > 0 ? (
          ideas.map((item) => (
            <div
              key={item.id}
              className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/60 hover:border-amber-500/50 transition flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-1 mb-2">
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-slate-700/60 text-slate-300 uppercase">
                    {item.source.replace('_', ' ')}
                  </span>
                  <div className="flex items-center gap-1 text-xs font-black text-amber-400">
                    <Star className="w-3.5 h-3.5 fill-amber-400" />
                    <span>{item.predicted_score}</span>
                  </div>
                </div>

                <h4 className="font-bold text-xs text-white leading-snug line-clamp-2 mb-2">
                  {item.title}
                </h4>

                <div className="flex items-center gap-1.5 text-[11px] text-slate-400">
                  <Clock className="w-3 h-3 text-slate-500" />
                  <span>Effort: <strong className="text-slate-300">{item.production_effort}</strong></span>
                </div>
              </div>

              <div className="mt-3 pt-2.5 border-t border-slate-700/40 flex items-center justify-between text-xs">
                <button
                  onClick={() => onScoreTitle && onScoreTitle(item.title)}
                  className="text-indigo-400 hover:text-indigo-300 font-medium text-[11px] transition"
                >
                  Evaluate CTR →
                </button>
                <span className="text-[10px] text-slate-500 capitalize">{item.status}</span>
              </div>
            </div>
          ))
        ) : (
          <div className="text-center py-6 text-slate-400 text-xs col-span-4">No ideas saved yet.</div>
        )}
      </div>
    </div>
  );
}
